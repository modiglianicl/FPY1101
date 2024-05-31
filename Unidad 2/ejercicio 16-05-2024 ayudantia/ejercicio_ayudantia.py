# Total compras e inventarios
total_compras = 0
inv_poleras = 0
inv_pantalones = 0
inv_chaqueta = 0
while True:
    try:
        # Menu Principal
        opcion_menu = int(input(f"Favor selecciona una opción : \n1.- Solicitar comprar \n2.- Pagar \n3.- ver Total \n4.- Salir\n"))
    except Exception as e:
        print(f"Favor ingresar un número entero entre 1 y 4. [Debug] Error : {e}")
        continue
    if opcion_menu >= 1 and opcion_menu <= 4:
        # Submenus
        ## Comienza menu "Solicitar compra"
        if opcion_menu == 1:
            try:
                sub_menu_compra = int(input("Que desea hacer? : \n1.- Comprar\n2.- Devolver compra\n3.- Volver al menú\n"))
                if sub_menu_compra >= 1 and sub_menu_compra <= 3:
                    ## Comienza Submenu 1 : Cantidad a comprar
                    if sub_menu_compra == 1:
                        try:
                            n_compras = int(input("¿Cuantos productos va a Comprar?\n"))
                            for i in range(0,n_compras):
                                try:
                                    opcion_compra = int(input(f"Selecciona un producto a comprar: \n1.- Polera $1000\n2.- Pantalón $2000\n3.- Chaqueta $5000\n"))
                                    if opcion_compra == 1:
                                        print(f"Usted compro una polera")
                                        total_compras += 1000
                                        inv_poleras += 1
                                        print(f"El total a pagar es de ${total_compras:,}")
                                    elif opcion_compra == 2:
                                        print(f"Usted compro un pantalón")
                                        total_compras += 2000
                                        inv_pantalones += 1
                                        print(f"El total a pagar es de ${total_compras:,}")
                                    elif opcion_compra == 3:
                                        print(f"Usted compro una chaqueta")
                                        total_compras += 5000
                                        inv_chaqueta +=1
                                        print(f"El total a pagar es de ${total_compras:,}")
                                    else:
                                        print(f"Algo occurió, su compra número {i+1} sera anulada, se procederá con compra n°{i+1}")
                                except Exception as e:
                                        print(f"Algo occurió, su compra número {i+1} sera anulada, se procederá con compra n°{i+1}. [Debug] Error : {e}")
                        except Exception as e:
                                    print(f"Algo occurió. [Debug] Error : {e}")
                    ## Termina Submenu 1 : Cantidad a comprar
                    ## Comienza Submenu 2 : Cantidad a devolver
                    elif sub_menu_compra == 2:
                         try:
                            sub_menu_devolver = int(input("Cuantos productos desea devolver?"))
                            if sub_menu_devolver > 0:
                                 for i in range(sub_menu_devolver):
                                    try:
                                        producto_devolver = int(input(f"Selecciona un producto a devolver: \n1.- Polera\n2.- Pantalón\n3.- Chaqueta\n"))
                                        if producto_devolver == 1:
                                            if inv_poleras > 0:
                                                print("Puede devolver")
                                                inv_poleras -= 1
                                                total_compras -= 1000
                                                print(f"El total a pagar es de ${total_compras:,}")
                                            else:
                                                print("No puede devolver. Usted no tiene poleras")
                                        elif producto_devolver == 2:
                                            if inv_pantalones > 0:
                                                print("Puede devolver")
                                                inv_pantalones -= 1
                                                total_compras -= 2000
                                                print(f"El total a pagar es de ${total_compras:,}")
                                            else:
                                                print("No puede devolver, no tiene pantalones.")
                                        elif producto_devolver == 3:
                                            if inv_chaqueta > 0:
                                                print("Puede devolver")
                                                inv_chaqueta -=1
                                                total_compras -= 5000
                                                print(f"El total a pagar es de ${total_compras:,}")
                                            else:
                                                print("No puede devolver, no tiene chaquetas.")
                                        else:
                                            print("Opción erronea.")
                                    except:
                                        print(f"Algo occurió. [Debug] Error : {e}")
                            else:
                                 print("Usted eligio no devolver nada.")
                         except Exception as e:
                              print(f"Algo occurió. [Debug] Error : {e}")
                    ## Termina Submenu 2 : Cantidad a devolver
                    ## Comienza Submenu 3 : Volver Al menu
                    elif sub_menu_compra == 3:
                         print("Volviendo al menú...")
                    ## Termina Submenu 3 : Volver Al menu
            except Exception as e:
                    print(f"Algo ocurrió. [Debug] error : {e}")
            ## Termina menu "Solicitar comprar"
        ## Menu 2 : Pagar
        elif opcion_menu == 2:
            print(f"Usted tiene una deuda de",f"${total_compras:,}".replace(",","."))
            try:
                pago = int(input("Cuanto desea pagar?"))
                if pago <= total_compras and pago > 0:
                    total_compras -= pago
                    print(f"Usted ha pagado",f"${pago:,}".replace(",","."))
                    print(f"Su saldo de deuda actual es :",f"${total_compras:,}".replace(",","."))
                else:
                    print("Debe ingresar un monto mayor a 0, igual o menor a su deuda, la cual es",f"${total_compras:,}".replace(",","."))
            except Exception as e:
                print(f"Algo occurió. [Debug] Error : {e}")
        ## Terminar menu 2 : Pagar
        ## Menu 3 : Mostrar deuda
        elif opcion_menu == 3:
            print(f"El total adeudado de su compra actual es de", f"${total_compras:,}".replace(",","."))
        ## Termina Menu 3
        ## Menu 4 : Salir
        elif opcion_menu == 4:
            print(f"Saliendo del programa....")
            quit() 
        else:
            print(f"Favor ingresar un número entero entre 1 y 4.")
        ## Termina Menu 4 : Salir
    

