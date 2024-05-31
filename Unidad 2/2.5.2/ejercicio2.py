# Inicializando programa
sw = 1
while sw != 0:
    print("1.- Ver mi Saldo")
    print("2.- Retirar Dinero")
    print("3.- Salir")
    try:
        opcion = int(input("Seleccione una opción : "))
    except:
        print("Valor erroneo.")
    
    if opcion == 1:
        confirmar_uno = input("Esta seguro que desea ver su saldo? (si/no)")
        if confirmar_uno.lower() == "si":
            print("Tiene un saldo de $500.000")
            volver_uno = int(input("Desea volver al menu (1) o salir del programa(2) ? : "))
            if volver_uno == 1:
                continue
            elif volver_uno == 2:
                print("Saliendo...")
                sw = 0
        elif confirmar_uno.lower() == "no":
            continue
    
    if opcion == 2:
        confirmar_dos = input("Esta seguro que desea retirar dinero? (si/no)")
        if confirmar_dos.lower() == "si":
            print("Retiro realizado")
            volver_dos = int(input("Desea volver al menu (1) o salir del programa(2) ? : "))
            if volver_dos == 1:
                continue
            elif volver_dos == 2:
                print("Saliendo...")
                sw = 0
        elif confirmar_dos.lower() == "no":
            continue
    
    if opcion == 3:
        confirmar_tres = input("Esta seguro que desea salir? (si/no)")
        if confirmar_tres.lower() == "si":
            print("Cierre de sesión exitoso, adiós")
            sw = 0
        elif confirmar_tres.lower() == "no":
            continue