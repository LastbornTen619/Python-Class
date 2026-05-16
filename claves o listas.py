        #1,2,3,4,5,
lista =[           "erick", "saul", "silvia"]
print(lista[0])
print (lista)

#for i in lista:
#    print(lista[i])

print(len(lista))
lista.append("juan")    #agrega a la lista
print(lista)
print(len(lista))

lista.remove("saul")    #remueve de forma esacta
print(lista)
print(len(lista))

lista.pop(1)           #remueve por slot
print(lista)
print(len(lista))

lista.reverse()       # voltea la lista 
print(lista)

lista.sort() #solo para un tipo de dato 
print(lista)

lista2 = [2,4,6,8,10,12]
lista3 = lista + lista2
print(lista3)