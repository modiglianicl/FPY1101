# Libreria necesaria
import csv

# Inicializa lista de datos
lista_biologia = []


# Lee el archivo y apenda solo en donde cada elemento 3 de cada fila sea "Biología"
with open('estudiantes.csv', 'r', newline='', encoding='utf-8') as archivo:
    datos = csv.reader(archivo)
    for i in datos:
        if i[2] == "Biología":
            lista_biologia.append(i)

# Variable donde guarda el promedio maximo
promedio_alto = 0

# Iteracion sobre cada alumno de biologia
for dato in lista_biologia:
    promedio = (float(dato[3]) + float(dato[4]) + float(dato[5]))/3 # Saca el promedio casteando float en cada nota, las cuales estan en indicies 3,4,5
    if promedio > promedio_alto: # Algoritmo de maximo
        promedio_alto = promedio

# Imprime el maximo
print(round(promedio_alto,2))