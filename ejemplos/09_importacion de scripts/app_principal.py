# Este es el archivo principal de la aplicacion.
# Aqui unimos lo que hace el frontend con lo que hace el backend.

from backend.servicio_saludo import crear_saludo
from frontend.pantalla import mostrar_mensaje


# Esta variable representa un dato que podria venir del usuario.
nombre_usuario = "Luis"


# Aqui llamamos una funcion del backend.
# El backend se encarga de preparar la informacion.
mensaje_final = crear_saludo(nombre_usuario)


# Aqui llamamos una funcion del frontend.
# El frontend se encarga de mostrar la informacion.
mostrar_mensaje(mensaje_final)