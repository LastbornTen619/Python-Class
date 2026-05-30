from pathlib import Path

import pandas as pd
import serial
from serial.tools import list_ports


# ============================================================
# CONFIGURACION GENERAL DEL EJEMPLO
# ============================================================
# Cambia este valor por el puerto serial donde este conectado tu dispositivo.
# En Windows normalmente se ve como COM3, COM4, COM5, etc.
PUERTO_SERIAL = "COM3"

# Esta es la velocidad de comunicacion del puerto serial.
# Debe coincidir con la configuracion del Arduino, ESP32 u otro equipo.
VELOCIDAD_BAUDIOS = 9600

# Cantidad de lecturas validas que el programa intentara guardar.
# Si quieres mas datos, puedes aumentar este numero.
CANTIDAD_LECTURAS = 10

# Tiempo maximo de espera al intentar leer una linea del puerto serial.
TIEMPO_ESPERA_SEGUNDOS = 2

# Separador esperado en cada linea recibida desde el puerto serial.
# Ejemplo de linea correcta: 25.4,60.8
SEPARADOR = ","

# Estos nombres seran usados como encabezados en el archivo Excel.
# Cambialos para reutilizar esta plantilla con otros sensores o variables.
NOMBRE_COLUMNA_1 = "variable_1"
NOMBRE_COLUMNA_2 = "variable_2"

# Ruta local del archivo Excel que se creara con las lecturas.
RUTA_ARCHIVO_EXCEL = Path(__file__).with_name("lecturas_serial.xlsx")


def mostrar_puertos_disponibles():
    # Esta funcion busca los puertos seriales detectados por el sistema.
    # Es util para que el estudiante identifique que puerto debe usar.
    print("Puertos seriales detectados en este equipo:")
    puertos = list(list_ports.comports())

    if not puertos:
        print("- No se detectaron puertos seriales disponibles.")
        print()
        return

    for puerto in puertos:
        print(f"- {puerto.device}: {puerto.description}")

    print()


def mostrar_resumen_plantilla():
    # Esta funcion resume la configuracion principal para que el estudiante
    # vea rapidamente que partes debe cambiar al reutilizar la plantilla.
    print("Plantilla de lectura serial a Excel")
    print(f"- Puerto configurado: {PUERTO_SERIAL}")
    print(f"- Baudios configurados: {VELOCIDAD_BAUDIOS}")
    print(f"- Columnas del Excel: {NOMBRE_COLUMNA_1}, {NOMBRE_COLUMNA_2}")
    print(f"- Archivo de salida: {RUTA_ARCHIVO_EXCEL.name}")
    print()


def abrir_puerto_serial(puerto_serial, velocidad_baudios):
    # Esta funcion abre el puerto serial del microcontrolador.
    # Se usa una sola vez para que el flujo del ejemplo sea facil de explicar.
    conexion_serial = serial.Serial(
        port=puerto_serial,
        baudrate=velocidad_baudios,
        timeout=TIEMPO_ESPERA_SEGUNDOS,
    )

    # reset_input_buffer limpia datos viejos que pudieron quedar en memoria.
    conexion_serial.reset_input_buffer()
    return conexion_serial


def convertir_linea_a_medicion(linea_recibida):
    # Esta funcion recibe una linea de texto y trata de separarla en dos valores.
    # Esperamos exactamente dos datos, por ejemplo: 25.4,60.8
    partes = linea_recibida.strip().split(SEPARADOR)

    if len(partes) != 2:
        raise ValueError(
            "La linea recibida no tiene exactamente dos valores separados por coma."
        )

    # Convertimos ambos textos a numeros decimales para poder analizarlos despues.
    valor_1 = float(partes[0])
    valor_2 = float(partes[1])

    # Regresamos un diccionario porque luego pandas puede convertirlo facilmente
    # en una tabla con dos columnas.
    return {
        NOMBRE_COLUMNA_1: valor_1,
        NOMBRE_COLUMNA_2: valor_2,
    }


def leer_mediciones_serial(conexion_serial, cantidad_lecturas):
    # Esta funcion lee varias lineas desde un puerto ya abierto.
    # Solo se guardan las lineas que tengan el formato correcto.
    mediciones = []

    print("Puerto abierto correctamente.")
    print("El microcontrolador debe enviar datos con este formato: 25.4,60.8")
    print()

    while len(mediciones) < cantidad_lecturas:
        # readline intenta leer hasta encontrar un salto de linea.
        # decode convierte los bytes recibidos a texto legible.
        linea = conexion_serial.readline().decode("utf-8", errors="ignore").strip()

        # Si no llego nada en el tiempo de espera, avisamos y seguimos intentando.
        if not linea:
            print("No llego una lectura en el tiempo esperado. Reintentando...")
            continue

        print(f"Linea recibida: {linea}")

        try:
            medicion = convertir_linea_a_medicion(linea)
            mediciones.append(medicion)
            print(
                "Lectura valida guardada: "
                f"{NOMBRE_COLUMNA_1}={medicion[NOMBRE_COLUMNA_1]}, "
                f"{NOMBRE_COLUMNA_2}={medicion[NOMBRE_COLUMNA_2]}"
            )
            print(f"Progreso: {len(mediciones)} de {cantidad_lecturas} lecturas")
            print()
        except ValueError as error:
            # Si la linea no tiene el formato esperado, la descartamos,
            # pero el programa sigue funcionando para fines educativos.
            print(f"Lectura descartada: {error}")
            print()

    return mediciones


def guardar_mediciones_en_excel(mediciones, ruta_archivo):
    # Esta funcion transforma la lista de mediciones en una tabla.
    # Cada diccionario se convierte en una fila del archivo Excel.
    tabla = pd.DataFrame(mediciones, columns=[NOMBRE_COLUMNA_1, NOMBRE_COLUMNA_2])

    # to_excel crea un archivo .xlsx con dos columnas configurables.
    # index=False evita que pandas agregue una columna extra con numeros de fila.
    tabla.to_excel(ruta_archivo, index=False)

    print("Archivo Excel creado correctamente.")
    print("Contenido guardado:")
    print(tabla)
    print()
    print(f"Ruta final del archivo: {ruta_archivo}")


def main():
    # Paso 1: mostrar los puertos disponibles para ayudar a configurar el ejemplo.
    mostrar_puertos_disponibles()
    mostrar_resumen_plantilla()

    try:
        # Paso 2: abrir el puerto serial donde esta conectado el microcontrolador.
        print(f"Abriendo el puerto {PUERTO_SERIAL} a {VELOCIDAD_BAUDIOS} baudios...")
        print()
        conexion_serial = abrir_puerto_serial(PUERTO_SERIAL, VELOCIDAD_BAUDIOS)

        # Paso 3: leer varias lineas desde el puerto serial abierto.
        with conexion_serial:
            mediciones = leer_mediciones_serial(conexion_serial, CANTIDAD_LECTURAS)

        # Paso 4: guardar esas lecturas en un archivo Excel con dos columnas.
        guardar_mediciones_en_excel(mediciones, RUTA_ARCHIVO_EXCEL)

    except serial.SerialException as error:
        # Este error suele aparecer cuando el puerto no existe, esta ocupado
        # o el cable/dispositivo no esta listo para comunicarse.
        print("No fue posible abrir o leer el puerto serial.")
        print(f"Detalle tecnico: {error}")
        print()
        print("Revisa estos puntos antes de volver a ejecutar:")
        print("1. Que el dispositivo este conectado.")
        print("2. Que PUERTO_SERIAL tenga el valor correcto, por ejemplo COM4.")
        print("3. Que la velocidad en baudios coincida con la del dispositivo.")
        print("4. Que el monitor serial de otro programa no este usando ese puerto.")


if __name__ == "__main__":
    # Librerias necesarias para ejecutar este ejemplo:
    # python -m pip install pyserial pandas openpyxl
    main()