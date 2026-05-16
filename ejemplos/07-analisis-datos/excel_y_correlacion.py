from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd


# Esta ruta apunta al archivo de Excel que usaremos para el ejemplo.
RUTA_EXCEL = Path(__file__).with_name("datos_estudiantes.xlsx")


def crear_excel_si_no_existe(ruta_archivo):
    # Esta funcion crea un archivo Excel de ejemplo si todavia no existe.
    # De esta forma el estudiante puede concentrarse en aprender a leerlo.
    if ruta_archivo.exists():
        return

    datos = pd.DataFrame(
        {
            "horas_estudio": [2, 3, 4, 5, 6, 7, 8],
            "asistencia": [60, 65, 72, 80, 85, 90, 95],
            "calificacion": [55, 60, 68, 75, 82, 90, 96],
        }
    )

    # to_excel guarda el DataFrame como un archivo de Excel.
    datos.to_excel(ruta_archivo, index=False)


def leer_datos_desde_excel(ruta_archivo):
    # read_excel lee un archivo .xlsx y lo convierte en un DataFrame.
    datos = pd.read_excel(ruta_archivo)
    return datos


def mostrar_datos(datos):
    # Esta funcion imprime los datos leidos para entender que contiene el Excel.
    print("Datos leidos desde Excel:")
    print(datos)
    print()


def calcular_correlacion(datos):
    # corr calcula que tan relacionadas estan las columnas numericas.
    # Si el valor se acerca a 1, la relacion es positiva fuerte.
    # Si se acerca a -1, la relacion es negativa fuerte.
    # Si se acerca a 0, casi no hay relacion lineal.
    matriz_correlacion = datos.corr(numeric_only=True)
    return matriz_correlacion


def mostrar_correlacion(matriz_correlacion):
    # Esta funcion muestra la matriz de correlacion en consola.
    print("Matriz de correlacion:")
    print(matriz_correlacion)
    print()


def graficar_dispersion(datos):
    # Esta grafica compara dos columnas para ver si parecen estar relacionadas.
    plt.figure(figsize=(8, 5))
    plt.scatter(datos["horas_estudio"], datos["calificacion"], color="darkgreen")
    plt.title("Relacion entre horas de estudio y calificacion")
    plt.xlabel("Horas de estudio")
    plt.ylabel("Calificacion")
    plt.grid(True)
    plt.tight_layout()
    plt.show()


def graficar_matriz_correlacion(matriz_correlacion):
    # Esta funcion convierte la matriz en una imagen para verla como mapa de calor.
    plt.figure(figsize=(7, 5))
    imagen = plt.imshow(matriz_correlacion, cmap="Blues", vmin=-1, vmax=1)

    plt.title("Mapa de calor de correlacion")
    plt.xticks(range(len(matriz_correlacion.columns)), matriz_correlacion.columns)
    plt.yticks(range(len(matriz_correlacion.index)), matriz_correlacion.index)

    # colorbar agrega una barra lateral para interpretar los colores.
    plt.colorbar(imagen)

    # Este bloque escribe los valores de correlacion dentro de cada celda.
    for fila in range(len(matriz_correlacion.index)):
        for columna in range(len(matriz_correlacion.columns)):
            valor = matriz_correlacion.iloc[fila, columna]
            plt.text(columna, fila, f"{valor:.2f}", ha="center", va="center")

    plt.tight_layout()
    plt.show()


def main():
    # Paso 1: crear el archivo Excel si no existe.
    crear_excel_si_no_existe(RUTA_EXCEL)

    # Paso 2: leer los datos del archivo.
    datos = leer_datos_desde_excel(RUTA_EXCEL)

    # Paso 3: mostrarlos en consola.
    mostrar_datos(datos)

    # Paso 4: calcular la correlacion entre las columnas numericas.
    matriz_correlacion = calcular_correlacion(datos)
    mostrar_correlacion(matriz_correlacion)

    # Paso 5: crear una grafica de dispersion.
    graficar_dispersion(datos)

    # Paso 6: mostrar la matriz de correlacion como grafica.
    graficar_matriz_correlacion(matriz_correlacion)


if __name__ == "__main__":
    main()