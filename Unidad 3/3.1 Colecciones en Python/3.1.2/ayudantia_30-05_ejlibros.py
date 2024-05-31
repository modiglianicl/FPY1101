libros = []

while True:
    try:
        print(f"Bienvenido a la biblioteca, seleccione una opcion")
        print(f"1. Añadir Libro")
        print(f"2. Buscar Libro")
        print(f"3. Eliminar libro")
        print(f"4. Salir")
        opcion_menu = int(input(""))
        # Comienza menu 1
        if opcion_menu == 1:
            while True:
                try:
                    libro_nuevo = input("Ingrese el nombre del libro : ")
                    if libro_nuevo in libros:
                        print(f"Ese libro ya existe en nuestra biblioteca!, pruebe con otro nombre.")
                    else:
                        libros.append(libro_nuevo.lower())
                        break
                except Exception as e:
                    print(f"Algo ocurrio... {e.with_traceback}")
        # Termina menu 1
        # Comienza menu 2
        elif opcion_menu == 2:
            while True:
                try:
                    libro_buscar = input("Ingrese el libro a buscar : ")
                    busqueda_estado = False
                    for libro in libros:
                        if libro.lower() == libro_buscar.lower():
                            busqueda_estado = True
                    if busqueda_estado:
                        print(f"El libro {libro_buscar} si está en nuestra biblioteca!")
                        busqueda_estado = False # Resetamos el estado de busqueda exitosa para la proxima busqueda
                        break
                    else:
                        print(f"Lo sentimos, ese libro no está en esta biblioteca")
                        break
                except Exception as e:
                    print(f"Error : {e.with_traceback}")
        # Termina menu 2
        # Comienza menu 3
        elif opcion_menu == 3:
            while True:
                try:
                    libro_borrar = input("Escriba el libro que quiere eliminar de la biblioteca : ")
                    borrar_exito = False
                    print(f"Se borraran todos los libros que tengan el nombre de '{libro_borrar}'")
                    for libro in libros:
                        if libro_borrar.lower() == libro.lower():
                            borrar_exito = True
                            libros.remove(libro)
                            print(f"Libro {libro} borrado")
                    if borrar_exito:
                        borrar_exito = False
                        print(f"Libro borrado!")
                        break
                    else:
                        print(f"Ese libro no se encontro, no se ha borrado nada")
                        break
                    
                except Exception as e:
                    print(f"Error : {e.with_traceback}")
        # Comienza menu 4
        elif opcion_menu == 4:
            print(f"Lista final : {libros}")
            break
        # Termina menu 4
    except ValueError:
        print(f"Debe ingresar un número!")
    except Exception as e:
        print(f"Error! : {e.with_traceback}")

