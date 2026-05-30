from pathlib import Path
import time

import pandas as pd
import paho.mqtt.client as mqtt


# ============================================================
# CONFIGURACION GENERAL DE LA PLANTILLA MQTT
# ============================================================
# Usa aqui la IP de tu PC Ubuntu donde correra Mosquitto.
# Ejemplo: 192.168.1.100
BROKER_MQTT = "192.168.1.100"
PUERTO_MQTT = 1883
CLIENTE_ID = "plantilla_python_mqtt"

# En esta plantilla usamos dos topicos distintos:
# 1. Python se suscribe al topico donde el ESP32 publica sensores.
# 2. Python publica mensajes en un topico de comandos para el ESP32.
TOPICO_SUSCRIPCION = "clase/esp32/sensores"
TOPICO_PUBLICACION = "clase/esp32/comandos"

# El mensaje esperado tiene dos valores separados por coma.
# Ejemplo: 24.5,61.2
SEPARADOR = ","
NOMBRE_COLUMNA_1 = "variable_1"
NOMBRE_COLUMNA_2 = "variable_2"

# Cantidad de mensajes que la plantilla intentara recibir antes de guardar.
CANTIDAD_MENSAJES = 5
TIEMPO_ESPERA_SEGUNDOS = 10

# Archivo de salida donde quedaran guardadas las lecturas MQTT.
RUTA_ARCHIVO_EXCEL = Path(__file__).with_name("lecturas_mqtt.xlsx")

# Si quieres, Python puede enviar un comando de prueba al ESP32 al conectarse.
PUBLICAR_COMANDO_DE_PRUEBA = True
MENSAJE_COMANDO_DE_PRUEBA = "ENCENDER_LED"


def crear_cliente_mqtt():
    # Esta funcion crea el cliente MQTT compatible con diferentes versiones
    # de la libreria paho-mqtt.
    if hasattr(mqtt, "CallbackAPIVersion"):
        cliente = mqtt.Client(
            mqtt.CallbackAPIVersion.VERSION2,
            client_id=CLIENTE_ID,
        )
    else:
        cliente = mqtt.Client(client_id=CLIENTE_ID)

    return cliente


def mostrar_resumen_plantilla():
    # Esta funcion resume la configuracion principal para reutilizarla.
    print("Plantilla de MQTT a Excel usando Mosquitto local")
    print(f"- Broker: {BROKER_MQTT}:{PUERTO_MQTT}")
    print(f"- Topico de sensores: {TOPICO_SUSCRIPCION}")
    print(f"- Topico de comandos: {TOPICO_PUBLICACION}")
    print(f"- Columnas del Excel: {NOMBRE_COLUMNA_1}, {NOMBRE_COLUMNA_2}")
    print(f"- Archivo de salida: {RUTA_ARCHIVO_EXCEL.name}")
    print()


def convertir_mensaje_a_fila(topico, mensaje):
    # Esta funcion transforma el texto recibido desde MQTT en una fila para Excel.
    partes = mensaje.strip().split(SEPARADOR)

    if len(partes) != 2:
        raise ValueError(
            "El mensaje MQTT debe contener exactamente dos valores separados por coma."
        )

    valor_1 = float(partes[0])
    valor_2 = float(partes[1])

    return {
        "topico": topico,
        NOMBRE_COLUMNA_1: valor_1,
        NOMBRE_COLUMNA_2: valor_2,
    }


def configurar_callbacks(cliente, mensajes_recibidos):
    # Esta funcion conecta la logica del programa con los eventos de MQTT.
    def al_conectar(cliente_mqtt, datos_usuario, flags, codigo_resultado, properties=None):
        print(f"Conectado al broker MQTT con resultado: {codigo_resultado}")
        cliente_mqtt.subscribe(TOPICO_SUSCRIPCION)
        print(f"Suscripcion realizada al topico: {TOPICO_SUSCRIPCION}")
        print()

    def al_recibir_mensaje(cliente_mqtt, datos_usuario, mensaje_mqtt):
        mensaje_texto = mensaje_mqtt.payload.decode("utf-8", errors="ignore").strip()
        print(f"Mensaje recibido en {mensaje_mqtt.topic}: {mensaje_texto}")

        try:
            fila = convertir_mensaje_a_fila(mensaje_mqtt.topic, mensaje_texto)
            mensajes_recibidos.append(fila)
            print(
                "Mensaje valido guardado: "
                f"{NOMBRE_COLUMNA_1}={fila[NOMBRE_COLUMNA_1]}, "
                f"{NOMBRE_COLUMNA_2}={fila[NOMBRE_COLUMNA_2]}"
            )
            print(
                f"Progreso: {len(mensajes_recibidos)} de {CANTIDAD_MENSAJES} mensajes"
            )
            print()
        except ValueError as error:
            print(f"Mensaje descartado: {error}")
            print()

    cliente.on_connect = al_conectar
    cliente.on_message = al_recibir_mensaje


def publicar_comando_de_prueba(cliente):
    # Esta funcion envia un comando simple al ESP32 para demostrar que
    # Python tambien puede publicar mensajes hacia el microcontrolador.
    if not PUBLICAR_COMANDO_DE_PRUEBA:
        return

    cliente.publish(TOPICO_PUBLICACION, MENSAJE_COMANDO_DE_PRUEBA)
    print(f"Comando publicado en {TOPICO_PUBLICACION}: {MENSAJE_COMANDO_DE_PRUEBA}")
    print()


def esperar_mensajes(mensajes_recibidos, cantidad_esperada, tiempo_maximo):
    # Esta funcion espera hasta recibir la cantidad de mensajes esperada
    # o hasta que se acabe el tiempo limite.
    tiempo_inicio = time.time()

    while len(mensajes_recibidos) < cantidad_esperada:
        if time.time() - tiempo_inicio > tiempo_maximo:
            print("Se alcanzo el tiempo maximo de espera para recibir mensajes.")
            print()
            break

        time.sleep(0.2)


def guardar_mensajes_en_excel(mensajes_recibidos, ruta_archivo):
    # Esta funcion crea la tabla final y la guarda en Excel.
    tabla = pd.DataFrame(
        mensajes_recibidos,
        columns=["topico", NOMBRE_COLUMNA_1, NOMBRE_COLUMNA_2],
    )
    tabla.to_excel(ruta_archivo, index=False)

    print("Archivo Excel creado correctamente.")
    print("Contenido guardado:")
    print(tabla)
    print()
    print(f"Ruta final del archivo: {ruta_archivo}")


def main():
    # Paso 1: mostrar los valores principales de la plantilla.
    mostrar_resumen_plantilla()

    # Paso 2: preparar la lista donde se iran guardando los mensajes validos.
    mensajes_recibidos = []

    # Paso 3: crear el cliente MQTT y conectar sus callbacks.
    cliente = crear_cliente_mqtt()
    configurar_callbacks(cliente, mensajes_recibidos)

    try:
        # Paso 4: conectar con el broker y empezar a escuchar mensajes.
        cliente.connect(BROKER_MQTT, PUERTO_MQTT, keepalive=60)
        cliente.loop_start()
        time.sleep(1)

        # Paso 5: publicar un comando de prueba hacia el ESP32.
        publicar_comando_de_prueba(cliente)

        # Paso 6: esperar a recibir mensajes para guardarlos despues en Excel.
        esperar_mensajes(
            mensajes_recibidos,
            cantidad_esperada=CANTIDAD_MENSAJES,
            tiempo_maximo=TIEMPO_ESPERA_SEGUNDOS,
        )

        # Paso 7: guardar en Excel lo que se recibio desde MQTT.
        guardar_mensajes_en_excel(mensajes_recibidos, RUTA_ARCHIVO_EXCEL)

    except Exception as error:
        print("No fue posible completar el ejemplo MQTT.")
        print(f"Detalle tecnico: {error}")
        print()
        print("Revisa estos puntos antes de volver a ejecutar:")
        print("1. Que Mosquitto este corriendo en tu PC Ubuntu.")
        print("2. Que la IP del broker y el puerto sean correctos.")
        print("3. Que el ESP32 y esta computadora esten en la misma red.")
        print("4. Que el ESP32 publique datos en el topico de sensores.")
    finally:
        try:
            cliente.loop_stop()
            cliente.disconnect()
        except Exception:
            pass


if __name__ == "__main__":
    # Librerias necesarias para ejecutar este ejemplo:
    # python -m pip install paho-mqtt pandas openpyxl
    main()