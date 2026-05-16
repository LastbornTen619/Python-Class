numero1 = float(input("Ingresa el primer numero: "))
numero2 = float(input("Ingresa el segundo numero: "))
operacion = input("Ingresa la operacion (+, -, *, /): ")

if operacion == "+":
    resultado = numero1 + numero2
    print("Resultado:", resultado)
elif operacion == "-":
    resultado = numero1 - numero2
    print("Resultado:", resultado)
elif operacion == "*":
    resultado = numero1 * numero2
    print("Resultado:", resultado)
elif operacion == "/":
    if numero2 != 0:
        resultado = numero1 / numero2
        print("Resultado:", resultado)
    else:
        print("No se puede dividir entre cero")
else:
    print("Operacion no valida")