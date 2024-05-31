nombres = []
apellidos = []

for i in range(3):
    nombre = input("Ingrese un nombre : ")
    apellido = input("Ingrese el apellido : ")
    nombres.append(nombre)
    apellidos.append(apellido)

for i in range(3):
    print(f"{nombres[i]} {apellidos[i]}")