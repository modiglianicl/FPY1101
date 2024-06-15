import csv

# Inicializar lista
datos_lista = []

# Obteniendo filas
with open('estudiantes.csv','r',newline='',encoding='utf-8') as archivo:
    datos = csv.reader(archivo)

    for fila in datos:
        datos_lista.append(fila)

# Agregando ultimo valor de cada fila a asistencias
asistencias = []
for fila in datos_lista:
    if fila[-1] == 'asistencia_final':
        continue
    asistencias.append(int(fila[-1]))

# Calculo promedio
promedio_asistencias = round(sum(asistencias) / len(asistencias),2)

# Promedio de notas por alumno y mostrar la más alta

notas_alumnos = []
lista_promedios = []
nota_mas_alta = 0.0
mejor_alumno = ""
for i in range(len(datos_lista)):
    if i == 0:
        continue
    nombre_alumno = datos_lista[i][0]
    apellido_alumno = datos_lista[i][1]
    nombre_completo = f"{nombre_alumno} {apellido_alumno}"
    suma_notas = float(datos_lista[i][3]) + float(datos_lista[i][4]) + float(datos_lista[i][5])
    prom_notas = round(suma_notas/3,2)
    # Creacion diccionario
    dato_apendar = {
        "alumno" : nombre_completo,
        "promedio" : prom_notas
    }
    notas_alumnos.append(dato_apendar)
    # Creacion lista para CSV
    datos_promedios = [nombre_alumno,apellido_alumno,prom_notas]
    lista_promedios.append(datos_promedios)
    # Deteccion mejor alumno
    if prom_notas > nota_mas_alta:
        nota_mas_alta = prom_notas
        mejor_alumno = f"{nombre_alumno} {apellido_alumno}"
    print(f"{nombre_alumno} {apellido_alumno} , promedio : {prom_notas}")

print(f"El mejor alumno es {mejor_alumno} con la nota {nota_mas_alta}")


# Escribiendo CSV

with open('promedios_ej3.csv','w',encoding='utf-8',newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['nombre','apellido','promedio'])
    writer.writerows(lista_promedios)

# Obteniendo mejor alumno revisando el diccionario

# test_promedio = 0.0
# mejor_alumno = ""

# for alumno in notas_alumnos:
#     print(list(alumno.items()))