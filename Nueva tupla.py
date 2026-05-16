colores = ('rojo', 'verde', 'azul', 'verde')

print("Tupla original:", colores)
print("Primer elemento:", colores[0])
print("Último elemento:", colores[-1])
print("Cantidad de elementos:", len(colores))
print("Cuántas veces aparece 'verde':", colores.count('verde'))
print("Posición de 'azul':", colores.index('azul'))

print("Recorrido con for:")
for color in colores:
    print(color)

nueva_tupla = colores + ("amarillo",)
print("Nueva tupla concatenada:", nueva_tupla)

lista_convertida = list(colores)
print("Tupla convertida a lista:", lista_convertida)