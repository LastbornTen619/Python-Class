def mostrar_bienvenida():
    print("Bienvenido al ejemplo de funciones")


def saludar(nombre):
    print(f"Hola, {nombre}")


def sumar(numero1, numero2):
    resultado = numero1 + numero2
    print("La suma es:", resultado)


mostrar_bienvenida()

saludar("Juan")

sumar(10, 5)

nombre_usuario = input("Ingresa tu nombre: ")
primer_numero = float(input("Ingresa el primer numero: "))
segundo_numero = float(input("Ingresa el segundo numero: "))

saludar(nombre_usuario)
sumar(primer_numero, segundo_numero)