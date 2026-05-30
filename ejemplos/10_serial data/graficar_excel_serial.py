from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd


# Esta ruta apunta al Excel creado por el ejemplo de lectura serial.
RUTA_ARCHIVO_EXCEL = Path(__file__).with_name("lecturas_serial.xlsx")

# Esta ruta sera usada para guardar la grafica como imagen.
RUTA_IMAGEN_GRAFICA = Path(__file__).with_name("grafica_lecturas_serial.png")


def obtener_columnas_numericas(datos):
    # Esta funcion detecta automaticamente las columnas numericas del Excel.
    # Eso vuelve al script mas reutilizable como plantilla.
    columnas_numericas = []

    for nombre_columna in datos.columns:
        if pd.api.types.is_numeric_dtype(datos[nombre_columna]):
            columnas_numericas.append(nombre_columna)

    return columnas_numericas


def leer_datos_desde_excel(ruta_archivo):
    # Esta funcion abre el archivo Excel y lo convierte en una tabla de pandas.
    datos = pd.read_excel(ruta_archivo)
    return datos


def mostrar_datos(datos):
    # Esta funcion imprime en consola las filas leidas del Excel.
    print("Datos leidos desde el archivo Excel:")
    print(datos)
    print()


def crear_columna_muestra(datos):
    # Esta funcion crea una columna numerica para usarla como eje X.
    # Cada fila representa una lectura recibida desde el microcontrolador.
    datos = datos.copy()
    datos["muestra"] = range(1, len(datos) + 1)
    return datos


def crear_y_guardar_grafica(datos, ruta_imagen):
    # Como esta plantilla debe adaptarse a diferentes sensores, elegimos
    # automaticamente las dos primeras columnas numericas encontradas.
    columnas_numericas = obtener_columnas_numericas(datos)

    if len(columnas_numericas) < 2:
        raise ValueError(
            "El archivo necesita por lo menos dos columnas numericas para graficar."
        )

    columna_1 = columnas_numericas[0]
    columna_2 = columnas_numericas[1]

    # plt.figure crea el espacio donde se dibujara la grafica.
    plt.figure(figsize=(10, 5))

    # Dibujamos la primera columna numerica del archivo Excel.
    plt.plot(
        datos["muestra"],
        datos[columna_1],
        marker="o",
        linestyle="-",
        color="steelblue",
        label=columna_1,
    )

    # Dibujamos la segunda columna numerica del archivo Excel.
    plt.plot(
        datos["muestra"],
        datos[columna_2],
        marker="s",
        linestyle="-",
        color="darkorange",
        label=columna_2,
    )

    # Estos textos ayudan a explicar los ejes y el contenido de la grafica.
    plt.title("Lecturas recibidas desde el puerto serial")
    plt.xlabel("Numero de muestra")
    plt.ylabel("Valor recibido")
    plt.grid(True)
    plt.legend()
    plt.tight_layout()

    # savefig guarda la grafica como imagen en otro archivo.
    plt.savefig(ruta_imagen)

    # show abre una ventana con la grafica para verla en clase.
    plt.show()

    print(f"Grafica guardada en: {ruta_imagen}")


def main():
    # Paso 1: verificar si el archivo Excel existe.
    if not RUTA_ARCHIVO_EXCEL.exists():
        print("No se encontro el archivo lecturas_serial.xlsx.")
        print("Primero ejecuta el script serial_a_excel_usb.py para generar el Excel.")
        return

    # Paso 2: leer el archivo Excel.
    datos = leer_datos_desde_excel(RUTA_ARCHIVO_EXCEL)

    # Paso 3: mostrar los datos para revisar que el contenido sea correcto.
    mostrar_datos(datos)

    # Paso 4: agregar una columna con el numero de lectura.
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