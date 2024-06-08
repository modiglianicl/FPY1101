listaTuplas = []
conjuntoEdades = set()
for i in range(3):
    nombre = input("Dame un nombre : ")
    edad = int(input("Dame una edad : "))
    datos = (nombre,edad)
    listaTuplas.append(datos)

for i in range(len(listaTuplas)):
    conjuntoEdades.add(listaTuplas[i][1])


print(conjuntoEdades)