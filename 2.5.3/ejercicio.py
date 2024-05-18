# Parametros ejercicio
deuda = 100000

# Menu Principal
while True:
    try:
        selecMenu = int(input("1.- Pago de Tarjeta de Crédito \n2.- Simulación de Compras \n3.- Salir\n"))
        if selecMenu >= 1 and selecMenu <= 3:
            ## Empieza Sub menu : Pagar tarjeta
            if selecMenu == 1:
                if deuda == 0:
                    print(f"Usted no debe nada!")
                else: 
                    while True:
                        try:
                            totalPago = int(input(f"Cuanto desea pagar de su deuda?.Su deuda actual es de ${deuda:,}\n"))
                            if totalPago > 0 and totalPago <= deuda:
                                deuda -= totalPago
                                print(f"Pago realizado. Usted ahora debe ${deuda:,}")
                                break
                            else:
                                print(f"Debe de ingresar un monto mayor a 0 e igual o menor a su deuda actual :  ${deuda:,}")
                        except ValueError as e:
                            print(f"Debe de ingresar un numero!")
                        except Exception as e:
                            print(f"Algo ocurrio! Error: {e.with_traceback}")
                            print(f"Volviendo al menú principal...")
                            break
            ## Termina Sub menu : Pagar tarjeta
            ## Empieza Sub menu : Simular Compras
            elif selecMenu == 2:
                while True:
                    try:
                        cantidadCompras = int(input("Cuantas compras desea realizar\n"))
                        if cantidadCompras > 0:
                            for i in range(cantidadCompras):
                                try:
                                    valorCompra = int(input(f"Cual es el valor de la compra n°{i+1}\n"))
                                    if valorCompra > 0:
                                        deuda += valorCompra
                                    else:
                                        print(f"Debe de ingresar un número!, omitiendo compra n°{i+1}")
                                except ValueError as e:
                                    print(f"Debe de ingresar un número!, omitiendo compra n°{i+1}")
                                except Exception as e:
                                    print(f"Algo ocurrio! Error: {e.with_traceback}")
                                    print(f"Volviendo al menú principal...")
                                    break
                            break # Cuando termina el for termina el sub menu : Simular Compras
                        else:
                            print(f"Debe de elegir al menos una simulación.")
                    except ValueError as e:
                        print(f"Debe de ingresar un número!")
                    except Exception as e:
                        print(f"Algo ocurrio! Error: {e.with_traceback}")
                        print(f"Volviendo al menú principal...")
                        break
            ## Termina Sub menu : Simular Compras
                    
            elif selecMenu == 3:
                print(f"Terminando programa...")
                break
        else:
            print(f"Debe de ingresar un número entre 1 y 3 para su selección.")
    except ValueError as e:
        print(f"Error : Debe de ingresar un número entre 1 y 3.")
    except Exception as e:
        print(f"Algo ocurrió!. Terminando programa {e.with_traceback}")