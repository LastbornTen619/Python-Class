estudiante = {
    "nombre": "Ana",
    "edad": 20,
    "curso": "Python",
}

print("Diccionario original:", estudiante)
print("Nombre:", estudiante["nombre"])
print("Edad con get():", estudiante.get("edad"))

estudiante["ciudad"] = "Bogota"
print("Agrega ciudad:", estudiante)

estudiante["edad"] = 21
print("Actualiza edad:", estudiante)

print("Claves:", list(estudiante.keys()))
print("Valores:", list(estudiante.values()))
print("Elementos:", list(estudiante.items()))

valor_curso = estudiante.pop("curso")
print("Valor eliminado con pop('curso'):", valor_curso)
print("Diccionario despues de pop():", estudiante)

print("Recorrido con for:")
for clave, valor in estudiante.items():
    print(clave, ":", valor)