
def registrate():
    print("bienvenido a mi programa")
    print("ingrese su nombre: ")
    nombre = input()
    print("ingrese su edad: ")
    edad = input()
    print("ingrese su correo: ")
    correo = input()
    print("ingresa tu contraseña: ")
    contraseña = input()
    print("registro exitoso")
    print("deseas agregar otro usuario? (si/no)")
    respuesta = input()
    if respuesta == "si":
        registrate()
    else:
        print("gracias por usar mi programa")
registrate()


