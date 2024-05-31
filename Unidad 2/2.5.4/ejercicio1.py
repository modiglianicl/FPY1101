# Estado inicial Luces
patio = False
sala = False
pasillo = False
jardin = False

# Menu
while True:
    print("1.- Encender/Apagar luces Patio (Alternado)")
    print("2.- Encender/Apagar luces Sala (Alternado)")
    print("3.- Encender/Apagar luces Pasillo (Alternado)")
    print("4.- Encender/Apagar luces Jardín (Alternado)")
    print("5.- Encender todo (Alternado)")
    print("6.- Apagar todo (Alternado)")
    print("7.- Salir del sistema")
    try:
        accion = int(input("Ingrese la opción deseada: "))
        if accion == 1:
            patio = not patio
            print("El patio ahora esta :","Encendido" if patio else "Apagado")
        elif accion == 2:
            sala = not sala
            print("La sala ahora esta :","Encendida" if sala else "Apagada")
        elif accion == 3:
            pasillo = not pasillo
            print("El pasillo ahora esta :","Encendido" if pasillo else "Apagado")
        elif accion == 4:
            jardin = not jardin
            print("El jardín ahora esta :","Encendido" if jardin else "Apagado")
        elif accion == 5:
            patio = True
            sala = True
            pasillo = True
            jardin = True
            print("Todas las luces han sido prendidas!")
        elif accion == 6:
            patio = False
            sala = False
            pasillo = False
            jardin = False
            print("Todas las luces han sido apagadas!")
        elif accion == 7:
            print("Hasta pronto...")
            break
    except ValueError as e:
        print(f"Debe de ingresar un número entre 1 y 7!")