numeros = [10, 20, 30, 40]

print("Lista original:", numeros)
print("Primer elemento:", numeros[0])
print("Ultimo elemento:", numeros[-1])
print("Cantidad de elementos:", len(numeros))

numeros.append(50)
print("append(50):", numeros)

numeros.insert(1, 15)
print("insert(1, 15):", numeros)

numeros.remove(30)
print("remove(30):", numeros)

valor_eliminado = numeros.pop()
print("pop():", valor_eliminado)
print("Lista despues de pop():", numeros)

numeros.sort()
print("sort():", numeros)

print("Recorrido con for:")
for numero in numeros:
    print(numero)