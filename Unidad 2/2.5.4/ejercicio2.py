while True:
    print("**********Menú**********")
    print("1.- Pagar con tarjeta de crédito")
    print("2.- Pagar con PayPal")
    print("3.- Pagar con transferencia")
    print("4.- Cancelar")
    print("5.- Salir")
    try:
        ## Comienza Menu Principal
        opcionMenu = int(input("Ingrese la opción deseada : "))
        ## Comienza Sub Menu : Pago con T.de Credito
        if opcionMenu == 1:
            while True:
                try:
                    tarjetaCredito = input("Ingrese el numero de su tarjeta de credito.\n")
                    titularTarjeta = input("Ingrese su nombre como aparece en su T.de credito.\n")
                    mesVencimiento = int(input("Ingrese numero de mes de vencimiento de su T.de Credito.\n"))
                    anioVencimiento = int(input("Ingrese numero de año de vencimiento de su T.de Credito.\n"))
                    if len(str(mesVencimiento)) != 2 or len((str(anioVencimiento))) !=2:
                        print("El mes o año de vencimiento no debe superar dos digitos.")
                    else:
                        print(f"Muchas gracias por su pago!.")
                        quit()
                except ValueError as e:
                    print(f"Debe de ingresar un dato valido!")
                except Exception as e:
                    print(f"Error, favor intente denuevo. Error {e.with_traceback}")
        ## Termina Sub Menu : Pago con T.de Credito   
        elif opcionMenu == 2:
            while True:
                try:
                    paypalUser = input("Ingrese su usario de Paypal.\n")
                    paypalPassword = input("Ingrese su contraseña de Paypal.\n")
                    print(f"Gracias por su pago!.")
                    quit()
                except Exception as e:
                    print(f"Se encontró un error, volviendo al menu principal!. Error: {e.with_traceback}")
                    break
        elif opcionMenu == 3:
            print(f"Para pagos con transferencia estos son los datos:")
            print(f"Cuenta : 123123")
            print(f"Correo : asdasd@correo.com")
        elif opcionMenu == 4:
            print("Cancelar?")
            break
        elif opcionMenu == 5:
            print("Salir?")
            break
        else:
            print(f"Opción no valida, debe de ingresar un número entre 1 y 5!.")
         ## Termina Menu Principal
    except ValueError as e:
        print(f"Debe ingresar un número entre 1 y 5!")
    except Exception as e:
        print(f"Algo ocurrió! Error : {e.with_traceback}")
