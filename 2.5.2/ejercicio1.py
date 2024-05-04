# Puntos Acumulados
sw = 1
puntos = 100000

# Programa
while sw == 1:
    print("1.- Ver mis puntos")
    print("2.- Gastar mis puntos")
    print("3.- Salir")
    opcion = int(input("Selecciona una opción: "))

    if opcion == 1:
        print(f"Sus puntos actuales son", f"{puntos:,}".replace(',','.'))
    elif opcion == 2:
        print("Seleccione el producto a canjear")
        print("1.- Gift Card de $10.000, valor de 10.000 puntos")
        print("2.- Secadora de pelo, valor de : 25.000 puntos")
        print("3.- Disco duro portátil, valor de: 30.000 puntos")
        print("4.- Volver al menú principal.")
        opcion_puntos = int(input("Seleccione opción : "))
        if opcion_puntos == 1:
            if puntos >= 10000:
                puntos -= 10000
                print(f"Gift card canjeada, ud ha gastado 10.000 puntos, su saldo actual de puntos es de {puntos:,} puntos.")
            else:
                print(f"Ud no tiene 10.000 puntos, ud actualmente tiene {puntos:,} puntos.")
        elif opcion_puntos == 2:
            if puntos >= 25000:
                puntos -= 25000
                print(f"Secadora de pelo canjeada, ud ha gastado 25.000 puntos, su saldo actual de puntos es de {puntos:,} puntos.")
            else:
                print(f"Ud no tiene 25.000 puntos, ud actualmente tiene {puntos:,} puntos.")
        elif opcion_puntos == 3:
            if puntos >= 30000:
                puntos -= 30000
                print(f"Disco duro portátil canjeado, ud ha gastado 30.000 puntos, su saldo actual de puntos es de {puntos:,} puntos.")
            else:
                print(f"Ud no tiene 30.000 puntos, ud actualmente tiene {puntos:,} puntos.")
        elif opcion_puntos == 4:
            continue
    elif opcion == 3:
        print("Saliendo programa")
        break
    else:
        print("Opción no válida.")







