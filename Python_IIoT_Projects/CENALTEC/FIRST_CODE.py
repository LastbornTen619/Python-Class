nombre = str(input("¿Cual es tu nombre? "))
print("Hola, " + nombre + " Bienvenido a Python")
edad = int(input("¿Que edad tienes? "))
resultado = float
opcion = 0

while opcion != 5: 
    opcion = int(input("¿Que operacion deseas agregar? 1: Suma, 2: Resta, 3: Multiplicacion, 4: Division, 5: Salir: "))
    if opcion == 1:
        a = int(input("Tu primer numero es:"))
        b = int(input("Tu segundo numero es:"))
        resultado = a + b
        print("El resultado de la suma es: ", resultado)

    elif opcion == 2:
        a = int(input("Tu primer numero es:"))
        b = int(input("Tu segundo numero es:"))
        resultado = a - b
        print("El resultado de la resta es: ", resultado)
    
    elif opcion == 3:
        a = int(input("Tu primer numero es:"))
        b = int(input("Tu segundo numero es:"))
        resultado = a * b
        print("El resultado de la multiplicacion es: ", resultado)
    
    elif opcion == 4:
        a = int(input("Tu primer numero es:"))
        b = int(input("Tu segundo numero es:"))
        if b != 0:
            resultado = a / b
            print("El resultado de la division es: ", resultado)
        else:
            print("Error: Division por cero no permitido")
    elif opcion == 5:
            print("Adios...:(")
            break