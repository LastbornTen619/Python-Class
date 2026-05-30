from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd


# Esta ruta apunta al Excel creado por el ejemplo de MQTT.
RUTA_ARCHIVO_EXCEL = Path(__file__).with_name("lecturas_mqtt.xlsx")

# Esta ruta sera usada para guardar la grafica como imagen.
RUTA_IMAGEN_GRAFICA = Path(__file__).with_name("grafica_lecturas_mqtt.png")


def leer_datos_desde_excel(ruta_archivo):
    # Esta funcion abre el archivo Excel y lo convierte en una tabla de pandas.
    datos = pd.read_excel(ruta_archivo)
    return datos


def mostrar_datos(datos):
    # Esta funcion imprime las filas leidas desde el Excel.
    print("Datos leidos desde el archivo Excel:")
    print(datos)
    print()


def obtener_columnas_numericas(datos):
    # Esta funcion detecta las columnas numericas para que la plantilla
    # pueda reutilizarse con distintos sensores o topicos.
    columnas_numericas = []

    for nombre_columna in datos.columns:
        if pd.api.types.is_numeric_dtype(datos[nombre_columna]):
            columnas_numericas.append(nombre_columna)

    return columnas_numericas


def crear_columna_muestra(datos):
    # Esta funcion crea una columna con el numero de muestra recibido.
    datos = datos.copy()
    datos["muestra"] = range(1, len(datos) + 1)
    return datos


def crear_y_guardar_grafica(datos, ruta_imagen):
    # Elegimos automaticamente las dos primeras columnas numericas.
    columnas_numericas = obtener_columnas_numericas(datos)

    if len(columnas_numericas) < 2:
        raise ValueError(
            "El archivo necesita por lo menos dos columnas numericas para graficar."
        )

    columna_1 = columnas_numericas[0]
    columna_2 = columnas_numericas[1]

    # plt.figure crea el espacio donde se dibujara la grafica.
    plt.figure(figsize=(10, 5))

    # Dibujamos la primera variable numerica del archivo.
    plt.plot(
        datos["muestra"],
        datos[columna_1],
        marker="o",
        linestyle="-",
        color="seagreen",
        label=columna_1,
    )

    # Dibujamos la segunda variable numerica del archivo.
    plt.plot(
        datos["muestra"],
        datos[columna_2],
        marker="s",
        linestyle="-",
        color="tomato",
        label=columna_2,
    )

    # Estos textos ayudan a explicar los ejes y el contenido de la grafica.
    plt.title("Lecturas recibidas desde MQTT")
    plt.xlabel("Numero de muestra")
    plt.ylabel("Valor recibido")
    plt.grid(True)
    plt.legend()
    plt.tight_layout()

    # savefig guarda la grafica como una imagen.
    plt.savefig(ruta_imagen)
    plt.show()

    print(f"Grafica guardada en: {ruta_imagen}")


def main():
    # Paso 1: verificar si el Excel existe.
    if not RUTA_ARCHIVO_EXCEL.exists():
        print("No se encontro el archivo lecturas_mqtt.xlsx.")
        print("Primero ejecuta el script mqtt_a_excel.py para generar el Excel.")
        return

    # Paso 2: leer el archivo Excel.
    datos = leer_datos_desde_excel(RUTA_ARCHIVO_EXCEL)

    # Paso 3: mostrar en consola los datos que luego se van a graficar.
    mostrar_datos(datos)

    # Paso 4: agregar una columna de muestra.
    datos_con_muestra = crear_columna_muestra(datos)

    # Paso 5: crear la grafica y guardarla como imagen.
    try:
        crear_y_guardar_grafica(datos_con_muestra, RUTA_IMAGEN_GRAFICA)
    except ValueError as error:
        print(f"No fue posible crear la grafica: {error}")


if __name__ == "__main__":
    # Librerias necesarias para ejecutar este ejemplo:
    # python -m pip install pandas matplotlib openpyxl
    main()