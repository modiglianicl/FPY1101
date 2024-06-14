# Ayudantia online del 13-06
# Construir un sistema de libreria que tenga las siguientes opciones :
#  1.- Agregar libro
#  2. Buscar libro
#  3.- Mostrar libros
#  4.- editar
#  5.- Salir
# Utilizar diccionarios

# Ejemplo
# libros = {
#     'id_producto' : id,
#     'nombre' : 'quijote',
#     'desc' : 'juanito',
#     'cantidad' : 10
# }

libros = {}
contador = 1
while True:
    print(f"1.- Agregar Libro")
    print(f"2.- Buscar Libro")
    print(f"3- Mostrar Libro")
    print(f"4.- Editar")
    print(f"5.- Salir")
    
    op = int(input("Seleccione una opción : ")) #####

    if op == 1:
        # Pedimos valores al usuario
        nombreLibro = input("Ingrese el nombre del libro : ")
        descLibro = input("Ingrese descripción del libro : ")
        stockLibro = int(input("Ingrese el stock del libro : ")) #####
        # Construimos un valor unico para los datos del diccionario
        idLibro = f'PID{contador}'
        libros[idLibro] = {
            'nombre' : nombreLibro,
            'descripcion' : descLibro,
            'stock' : stockLibro
        }
        contador += 1
    elif op == 2:
        librobuscado = input("Ingrese el libro a buscar : ")
        for producto_id, detalle in libros.items():
            if detalle['nombre'].lower().strip() == librobuscado.lower().strip():
                print("Libro encontrado!")
                print(detalle)
            else:
                print("Libro no encontrado")

    elif op == 3:
        print(libros)

    elif op == 4:
        librobuscado = input("Ingrese el libro a buscar : ")
        for producto_id, detalle in libros.items():
            if detalle['nombre'].lower().strip() == librobuscado.lower().strip():
                print(f"Que quieres editar : ")
                print(f"1.- Nombre")
                print(f"2.- Descripcion")
                print(f"3.- Cantidad")
                op_editar = int(input("Elije una opción : "))

                if op_editar == 1:
                    n_nombre = input("Ingresa el nuevo nombre del libro")
                    detalle['nombre'] = n_nombre
                    print("Libro editado")
                    print(libros)
                elif op_editar == 2:
                    n_descripcion = input("Ingresa la nueva descripción : ")
                    detalle['descripcion'] = n_descripcion
                    print("Libro editado")
                    print(libros)
                elif op_editar == 3:
                    n_cantidad = int(input("Ingresa la nueva cantidad : "))
                    detalle['stock'] = n_cantidad
                    print("Libro editado")
                    print(libros)
    elif op == 5:
        print("Terminando programa...")
        break
