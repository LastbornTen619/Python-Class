colores = ("Rojo", "Verde", "Azul", "Verde")

print("Tupla original:", colores)
print("Primer elemento", colores[0])
print("Ultimo elemento", colores[-1])
print("Cantidad de elementos:", len(colores))
print("Cuantas veces aparece 'verde' : ", colores.count("Verde"))
print("Posicion de 'Azul' : ", colores.index("Azul"))

print("Recorrido con for:")
for color in colores:
    print(color)

nueva_tupla = colores + ("Amarillo")
print("Nueva tupla concatenada:", nueva_tupla)

lista_convertida = list(colores)
print("Tupla convertida a lista", lista_convertida)


'''def bienvenida():
    print("Bienvenido a la clase de Python")

def sumar(a, b):
    return a + b

bienvenida()
a = float(input("Ingresa el primer numero: "))
b = float(input("Ingresa el segundo numero: "))
resultado = sumar(a, b)
print("El resultado de la suma es: ", resultado)

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "Alexis",]
print(lista)

#for i in lista:
#   print(lista[i])

print(len(lista))
lista.append("Juan")
print(lista)
print(len(lista))

lista.remove(3)
print(lista)
print(len(lista))

lista.pop(0)
print(lista)
print(len(lista))'''




