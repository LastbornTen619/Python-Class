lista = [1, 2, 3, 4, 5,]
print(lista[0])
print(lista)

#for i in lista:
#   print(lista[i])

print(len(lista))
lista.append(3)
print(lista)
print(len(lista))

lista.remove(3) 
print(lista)
print(len(lista)) 
           
lista.pop(1)
print(lista)
print(len(lista))

lista.reverse()
print(lista)

lista.sort() # no se puede ordenar una lista que contiene diferentes tipos de datos
print(lista)

lista2 = [6, 7, 8, 9, 10]
lista3 = lista + lista2
print(lista3)

