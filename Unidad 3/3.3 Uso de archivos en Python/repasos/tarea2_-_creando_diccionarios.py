#Crear agenda telefonica donde la estructura del diccionario debe ser la siguiente:
#
#{
#    "nombre":{
#        "telefono" : string,
#        "email" : string,
#        "direccion" : string
#    }
#
#}
# PARTE 2, escribir datos en un CSV.
import csv
from pathlib import Path

agenda_telefonica = []

while True:
    # Pidiendo datos
    nombre = input("Cual es su nombre : ")
    telefono = input("ingrese su telefono, me da lo mismo el largo : ")
    email = input("ingrese su correo (bien porfavor) : ")
    direccion = input("Ingrese su dirección : ")
    try:
        estadoUsuario = bool(int(input("Estado usuario (Habilitado = 1 / No Habilitado = 0) : ")))
    except ValueError:
        print(f"El valor del estado debe ser 1 o 0.")
    # Creando el objeto/diccionario
    datosUsuario = { "nombre" : nombre,
        "telefono" : telefono,
        "email" : email,
        "direccion" : direccion,
        "estado" : estadoUsuario
    }
    # Apendamos el diccionario a la lista
    agenda_telefonica.append(datosUsuario)
    # Pregunamos si queremos agregar mas usuarios
    continuarDatos = int(input("Desea continuar ? : 1.Si 2.No "))
    if continuarDatos == 2:
        break

# Parte 2, traspasar datos agregados a un csv

# Obteniendo nombre columnas
columnas = [llaves for llaves in agenda_telefonica[0].keys()]
print(columnas)
# Nombre archivo
nombre_archivo = "agenda_telefonica.csv"
# Creando el writer
with open(f'{Path.cwd()}/{nombre_archivo}',"w") as csvfile:
    writer = csv.DictWriter(csvfile,fieldnames=columnas,lineterminator='\n')
    writer.writeheader()
    writer.writerows(agenda_telefonica)


# Imprimimos cada elemento de la lista
for i in range(len(agenda_telefonica)):
    print(agenda_telefonica[i])

