productos = []
valor_productos = []

while True:
    print(f"Bienvenido al menú de compras, seleccione una opción")
    print(f"1. Agregar productos")
    print(f"2. Ver Canasta")
    print(f"3. Ver Total")
    print(f"4. Salir")
    try:
        seleccion = int(input(""))
        # Comienza menu 1
        if seleccion == 1:
            while True:
                try:
                    print(f"¿Qué producto desea agregar a su canasta?")
                    print(f"1. Peras $500")
                    print(f"2. Manzanas $600")
                    print(f"3. Platanos $450")
                    print(f"4. Nueces $1000")
                    print(f"5. Lechuga $350")
                    seleccion_uno = int(input(""))
                    if seleccion_uno == 1:
                        productos.append('peras')
                        valor_productos.append(500)
                        print(f"Usted agrego peras a su canasta.")
                        break
                    elif seleccion_uno == 2:
                        productos.append('manzanas')
                        valor_productos.append(600)
                        print(f"Usted agrego manzanas a su canasta.")
                        break
                    elif seleccion_uno == 3:
                        productos.append('platanos')
                        valor_productos.append(450)
                        print(f"Usted agrego platanos a su canasta.")
                        break
                    elif seleccion_uno == 4:
                        productos.append('nueces')
                        valor_productos.append(1000)
                        print(f"Usted agrego nueces a su canasta.")
                        break
                    elif seleccion_uno == 5:
                        productos.append('lechuga')
                        valor_productos.append(350)
                        print(f"Usted agrego manzanas a su canasta.")
                        break
                    else:
                        print(f"Porfavor selecciona una opción correcta (número entre 1 y 5)")
                except ValueError:
                    print(f"Debe de seleccionar con un número su producto! entre el 1 y el 5.")
        # Termina menu 1
        # Comienza menu 2
        elif seleccion == 2:
            print(f"Su canasta consiste de {len(productos)} productos :")
            if len(productos) >= 1:  
                for i in range(len(productos)):
                    print(f"{i+1}.- {productos[i]} @ ${valor_productos[i]}")
            else:
                print(f"Usted no tiene productos en su canasta!")
        # Termina menu 2
        # Comienza menu 3
        elif seleccion == 3:
            print(f"El total de su canasta es de : CLP ${sum(valor_productos):,}")
        # Termina menu 3
        elif seleccion == 4:
            print(f"Terminando programa....")
            break
        else:
            print(f"Debe seleccionar un menu con un numero entre el 1 y el 4!")
    


    except ValueError:
        print(f"La opción seleccionada debe ser un número entre 1 y 4!")

