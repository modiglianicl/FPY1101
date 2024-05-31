
lista_nombre = []
nombre_con_mayor_tamano = ""

for i in range(3):
    nombre = input("Deme un nombre : \n")
    lista_nombre.append(nombre)
    print(len(nombre_con_mayor_tamano)<len(nombre))
    if(len(nombre_con_mayor_tamano) < len(nombre)):
        nombre_con_mayor_tamano = nombre

print(lista_nombre)
print(nombre_con_mayor_tamano)