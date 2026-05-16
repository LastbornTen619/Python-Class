lista = ["selena", "Maria", "Taylor"]
print(lista[0])
print(lista)

#for i in lista:
#    print(lista[i])

print(len(lista))
lista.append("Selena")
print(lista)
print(len(lista))

lista.remove("Taylor")
print(lista)
print(len(lista))

lista.pop()
print(lista)
print(len(lista))

lista.reverse()
print(lista)

lista.sort()
print(lista)
lista2 =  [6, 7, 8, 9, 10]
lista3 = lista + lista2
print(lista3)
