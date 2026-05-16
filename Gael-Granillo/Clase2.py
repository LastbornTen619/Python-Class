lista = ["Luis", "Maria", "Ana"]
print(lista[0])  # Imprime el primer elemento de la lista
print(lista) 

#for i in lista: 
#   print(lista[i])

print(len(lista))
lista.append("Juan")
print (lista) 
print (len(lista))

lista.remove("Maria")
print(lista)
print(len(lista))

lista.pop(2)
print(lista)
print(len(lista)) 

lista.reverse()
print(lista)

lista.sort()
print(lista)

lista2 = [6, 7, 8, 9, 10]
lista3 = lista + lista2
print(lista3)   
 # Imprime el sexto elemento de la lista