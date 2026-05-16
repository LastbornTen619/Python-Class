while True:
    print("\nCalculadora")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Salir")

    opcion = input("Elige una opcion: ")

    if opcion == "5":
        print("Programa finalizado")
        break

    if opcion in ["1", "2", "3", "4"]:
        numero1 = float(input("Ingresa el primer numero: "))
        numero2 = float(input("Ingresa el segundo numero: "))

        if opcion == "1":
            print("Resultado:", numero1 + numero2)
        elif opcion == "2":
            print("Resultado:", numero1 - numero2)
        elif opcion == "3":
            print("Resultado:", numero1 * numero2)
        elif opcion == "4":
            if numero2 != 0:
                print("Resultado:", numero1 / numero2)
            else:
                print("No se puede dividir entre cero")
    else:
        print("Opcion no valida")