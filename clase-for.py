usuarios = {}

def registrar_usuario():
    print("\n--- REGISTRO DE USUARIO ---")
    
    usuario = input("Crea un nombre de usuario: ")
    
    if usuario in usuarios:
        print("Ese usuario ya existe.")
        return
    
    contraseña = input("Crea una contraseña: ")
    
    usuarios[usuario] = contraseña
    print("Usuario registrado correctamente.")


def iniciar_sesion():
    print("\n--- INICIAR SESIÓN ---")
    
    usuario = input("Usuario: ")
    contraseña = input("Contraseña: ")
    
    if usuario in usuarios and usuarios[usuario] == contraseña:
        print(f"Bienvenido, {usuario}. Has iniciado sesión correctamente.")
    else:
        print("Usuario o contraseña incorrectos.")


def mostrar_usuarios():
    print("\n--- USUARIOS REGISTRADOS ---")
    
    if len(usuarios) == 0:
        print("No hay usuarios registrados.")
    else:
        for usuario in usuarios:
            print(f"- {usuario}")


def menu():
    while True:
        print("\n===== SISTEMA DE LOGIN =====")
        print("1. Registrar usuario")
        print("2. Iniciar sesión")
        print("3. Ver usuarios")
        print("4. Salir")
        
        opcion = input("Elige una opción: ")
        
        if opcion == "1":
            registrar_usuario()
        elif opcion == "2":
            iniciar_sesion()
        elif opcion == "3":
            mostrar_usuarios()
        elif opcion == "4":
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida. Intenta otra vez.")


menu()