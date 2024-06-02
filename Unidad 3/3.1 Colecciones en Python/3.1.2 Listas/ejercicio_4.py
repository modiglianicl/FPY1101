# Este tambien es parte de la ayudantia
# Usuario admin viene por defecto
usuarios = ["admin"]
password = ["admin"]
usuario_logeado = "" # Para dar la bienvenida en el menú


while True:
    try:
        if usuario_logeado: # Si alguien se logea le decimos su nombre
            print(f"Bienvenido {usuario_logeado}, seleccione una opcion : ")
        else:
            print(f"Bienvenido anonimo, seleccione una opcion : ")
        print(f"1.- Iniciar Sesion")
        print(f"2.- Registrar")
        print(f"3.- Eliminar usuario")
        print(f"4.- Salir")
        seleccion = int(input(""))
        if seleccion == 1:
            logear = 0
            while logear == 0:
                usuario = input("Ingrese usuario : ")
                indice_usuario = usuarios.index(usuario)
                if usuario in(usuarios):
                    while True:
                        pass_usuario = input("Ingrese contraseña : ")
                        if pass_usuario == password[indice_usuario]:
                            print(f"Contraseña correcta!, volviendo al menu")
                            usuario_logeado = usuarios[indice_usuario]
                            logear = 1
                            break
                        else:
                            print(f"Contraseña incorrecta!, intente denuevo!")
                else:
                    print(f"Usted no es usuario!, debe de registrarse")
                    break
        elif seleccion == 2:
            while True:
                usuario_nuevo = input("Ingrese su nombre de usuario a registrar (se registrará en minusculas): ")
                if usuario_nuevo.lower() in (usuarios):
                    print(f"Ese usuario ya esta usado!")
                else:
                    pass_nueva = input("Ingrese su contraseña : ")
                    password.append(pass_nueva)
                    usuarios.append(usuario_nuevo.lower()) # Todos los usuarios seran en minusculas
                    print(f"Usuarios registrados : {usuarios}")
                    break
        elif seleccion == 3:
            while True:
                usuario_borrar = input("Ingrese el nombre de usuario a borrar : ")
                if usuario_borrar in (usuarios):
                    print(f"Borrando usuario...")
                    # Tambien debemos de obtener el indice del usuario para borrar su contraseña!
                    pass_a_borrar = usuarios.index(usuario_borrar)
                    usuarios.remove(usuario_borrar)
                    del password[pass_a_borrar]
                    print(f"Usuarios actuales : {usuarios}")
                    print(f"Contraseñas actuales : {password}")
                    break
                else:
                    print(f"Ese usuario no exite!, volviendo al menú.")
        elif seleccion == 4:
            print(f"Terminando programa....")
            print(f"Usuarios finales : {usuarios}")
            print(f"Contraseñas finales : {password}")
            break
    except Exception as e:
        print(f"Algo ocurrio! : {e.with_traceback}")


            