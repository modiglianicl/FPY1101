import csv
import os

# datos

usuarios = [{
    'nombre' : "felipe",
    "edad" : 32,
    "ciudad" : "quilpue"
},
{
    "nombre" : "cesar",
    "edad" : 28,
    "ciudad" : "viña"
},
{
    "nombre" : "victor",
    "edad" : 22,
    "ciudad" : "villa alemana"
}]

# columnas

columnas = ["nombre","edad","ciudad"]

# nombre archivo

nombre_archivo = "usuarios.csv"

# escribiendo al csv

print(os.getcwd())

with open(f'{os.getcwd()}\\Unidad 3\\3.3 Uso de archivos en Python\\{nombre_archivo}',"w") as csvfile:
    # Creando objeto que escribe
    writer = csv.DictWriter(csvfile, fieldnames=columnas, lineterminator='\n')
    # Creando columnas
    writer.writeheader()
    # escribiendo filas (datos)
    writer.writerows(usuarios)