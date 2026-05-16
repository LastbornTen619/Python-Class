import matplotlib.pyplot as plt
import pandas as pd


def crear_datos_desde_listas():
    # Este ejemplo empieza con listas normales de Python.
    meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio"]
    ventas = [1200, 1350, 1280, 1600, 1750, 1900]

    # Con pandas podemos convertir esas listas en una tabla de datos.
    datos = pd.DataFrame({"mes": meses, "ventas": ventas})
    return datos


def mostrar_resumen(datos):
    # Esta funcion muestra informacion basica del DataFrame.
    print("Datos creados desde listas y convertidos a DataFrame:")
    print(datos)
    print()

    print("Primeras filas del archivo:")
    print(datos.head())
    print()

    print("Resumen numerico:")
    print(datos.describe())
    print()


def crear_grafica(datos):
    # plt.figure crea un espacio nuevo para dibujar la grafica.
    plt.figure(figsize=(10, 5))

    # plt.plot dibuja una linea usando una columna para el eje X y otra para el eje Y.
    plt.plot(
        datos["mes"],
        datos["ventas"],
        marker="o",
        linestyle="-",
        color="steelblue",
    )

    # Estos metodos agregan contexto visual a la grafica.
    plt.title("Ventas mensuales")
    plt.xlabel("Mes")
    plt.ylabel("Ventas")
    plt.grid(True)

    # tight_layout ajusta los espacios para que el contenido no se encime.
    plt.tight_layout()

    # show abre la ventana con la grafica.
    plt.show()


def main():
    # Paso 1: crear los datos a partir de listas de Python.
    datos = crear_datos_desde_listas()

    # Paso 2: mostrar la informacion en consola.
    mostrar_resumen(datos)

    # Paso 3: graficar los datos.
    crear_grafica(datos)


if __name__ == "__main__":
    main()