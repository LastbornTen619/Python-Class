for i in range (1,6):
    print(i)    

a = float (input("Hola, dame un numero para sumar"))
b = float (input("Dame el segundo numero"))

def sumar(a, b):
    return a + b

resultado = sumar(a, b)   # aquí llamamos la función y guardamos el resultado
print(resultado)          # imprime la suma de a y b

colores = ("rojo", "verde", "azul", "amarillo", "morado")

print("Los colores en recorrido con for son:" )
for color in colores:
    print(color)
    
