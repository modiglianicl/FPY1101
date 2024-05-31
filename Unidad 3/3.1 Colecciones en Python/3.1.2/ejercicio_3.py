nombres = []
seguir = "si"
while seguir == "si":
    nombre = input("Ingrese un nombre : ")
    nombres.append(nombre)
    while True:
        seguir = input("Desa seguir ? (si/no)")
        if seguir.lower() == "no":
            print(f"Terminando...")
            seguir = "no"
            break
        elif seguir.lower() == "si":
            break
        elif seguir.lower() not in ("si","no"):
            print(f"Debe escribir sí o no.")

# Banderas
indice_menor = 0
minimo = 0

# Borrando el menor
if len(nombres) >= 2:
    for i in range(len(nombres)):
        largo_nombre = len(nombres[i])
        if i == 0:
            minimo = largo_nombre
        if largo_nombre < minimo:
            minimo = largo_nombre
            indice_menor = i
    # Imprimimos lo que hacemos
    print(f"Eliminando nombre en indice {indice_menor} : '{nombres[indice_menor]}'")
    del nombres[indice_menor]
    print(nombres)
    
else:
    print(f"La lista solo tiene un nombre ,no borraré nada. Aquí va la lista : ")
    print(nombres)

