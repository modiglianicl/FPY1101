import csv
import json

def obtener_datos_csv(nombre_archivo):
    lista_datos_raw = []
    with open(nombre_archivo,'r',newline='',encoding='utf-8') as archivo:
        datos = csv.reader(archivo)
        for i in datos:
            lista_datos_raw.append(i)
    return lista_datos_raw

def obtener_el_promedio_mas_alto(datos):
    nota_alta = 0.0

    for i in range(1,len(datos)):
        promedio_alumno = (float(datos[i][3]) + float(datos[i][4]) +float(datos[i][5])) / 3
        if promedio_alumno > nota_alta:
            nota_alta = promedio_alumno
    
    return nota_alta