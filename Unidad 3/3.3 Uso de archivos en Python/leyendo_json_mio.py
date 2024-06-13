# Ejercicio en donde calculo directamente metricas de los usuarios desde un archivo JSON.
# El ultimo ejercicio obtiene todos los IMC por edad en un diccionario y luego calcula sus promedios para finalmente escribirlos en un CSV.

# Librerias
import json
from pathlib import Path
import csv

f = open(f'{Path.cwd()}\\datos.json')


data = json.load(f)

data_usuarios = data['usuarios']

# Promedio edad gente mayor a 24
edad_mayores = []
for i in (range(len(data_usuarios))):
    if int(data_usuarios[i]['edad']) > 24:
        edad_mayores.append(int(data_usuarios[i]['edad']))
        
print(f"La edad promedio de los mayores a 24 es de {round(sum(edad_mayores)/len(edad_mayores),2)}")

# Promedio IMC de los usuarios
imc_usuarios = []
for i in (range(len(data_usuarios))):
    imc_usuarios.append(data_usuarios[i]['perfil_salud']['IMC'])

print(f"El IMC promedio es de  {round(sum(imc_usuarios)/len(imc_usuarios),2)}")

# Obteniendo edades unicas
edades_usuarios = []
for i in range(len(data_usuarios)):
    edad = int(data_usuarios[i]['edad'])
    if edad not in edades_usuarios:
        edades_usuarios.append(edad)
edades_usuarios.sort()
print(f"Las edades de los usuarios : {edades_usuarios}")

########################## Ejercicio Analisis de datos JSON a CSV ##########################

# Obteniendo el promedio IMC de cada edad (guardado en un json/diccionario)

imc_usuarios_edad = {}
edades_existentes = set()

for edad in edades_usuarios:
    for i in range(len(data_usuarios)):
        edad_usuario = data_usuarios[i]['edad']
        if int(edad) == int(edad_usuario):
            imc = data_usuarios[i]['perfil_salud']['IMC']
            if len(imc_usuarios_edad) == 0: # Si no hay ningun elemento
                print(f"Usuario {i}")
                print(f"lista menor a 0")
                imc_usuarios_edad[edad] = [imc]
                edades_existentes.add(edad)
            elif len(imc_usuarios_edad) >= 1: # Si ya hay un elemento
                if int(edad) not in edades_existentes: # Chequeamos si esa llave no se ha analizado
                    print(f"Usuario {i} : Su edad es nueva")
                    imc_usuarios_edad[edad] = [imc]
                    edades_existentes.add(edad)
                    print(imc_usuarios_edad)
                else:
                    imc_usuarios_edad[edad].append(imc)


print(f"IMC De todos los usuarios por edad : {imc_usuarios_edad}")
print(f"Lista edades existentes : {edades_existentes}")

# Obteniendo promedio por edad dentro del diccionario

imd_promedios = {}

for edad,promedios in imc_usuarios_edad.items():
    imd_promedios[edad] = round(sum(promedios) / len(promedios),2)

print(imd_promedios)

# Pasando los datos a un CSV

nombre_archivo = f'{Path.cwd()}\\imc_por_edad.csv'

with open(nombre_archivo, 'w', newline='') as csvfile:
     columnas = ['Edad', 'IMCs']
     writer = csv.DictWriter(csvfile, fieldnames=columnas)

     writer.writeheader() # Escribimos columnas (first row)
     for edad, imcs in imd_promedios.items(): # Iteramos items diccionarios
         writer.writerow({'Edad': edad, 'IMCs': imcs})