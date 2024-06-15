import csv

lista_biologia = []



with open('estudiantes.csv', 'r', newline='', encoding='utf-8') as archivo:
    datos = csv.reader(archivo)
    for i in datos:
        if i[2] == "Biología":
            lista_biologia.append(i)

suma = 0
promedio_alto = 0

for dato in lista_biologia:
    promedio = (float(dato[3]) + float(dato[4]) + float(dato[5]))/3
    if promedio > promedio_alto:
        promedio_alto = promedio

print(promedio_alto)