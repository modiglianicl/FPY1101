import csv
import json

lista_diccionarios = []

with open('alumnos_detallado.csv','r',encoding='utf-8') as archivo:
    datos_raw = csv.reader(archivo)

    for i in datos_raw:
        if i[0] == 'rut':
            continue
        datos_dict = {
            'rut' : i[0],
            'nombre' : i[1],
            'apellido' : i[2],
            'curso' : i[3],
            'asignatura' : i[4],
            'notas' : {
                'nota1' : i[5],
                'nota2' : i[6],
                'nota3' : i[7]
            },
            'asistencia' : i[8]
        }
        lista_diccionarios.append(datos_dict)

# Mejor alumno por asignatura

# Obteniendo asignaturas
asignaturas = []

for i in lista_diccionarios:
    asignaturas.append(i['asignatura'])
# Creamos conjunto para eliminar duplicados
asignaturas = set(asignaturas)

promedio_alumno_asignatura = []

for i in lista_diccionarios:
    for j in asignaturas:
        if i['asignatura'] == j:
            datos = {
                'rut' : i['rut'],
                'asignatura' : j,
                'curso' : i['curso'],
                'promedio_alumno' : [(float(i['notas']['nota1'])+
                            float(i['notas']['nota2'])+
                            float(i['notas']['nota3']))/3]
            }
            promedio_alumno_asignatura.append(datos)

# Inicializando cada asignatura con un 0
mejores_promedios_asignaturas = {
}

for i in asignaturas:
    mejores_promedios_asignaturas[i] = 0.0

print(mejores_promedios_asignaturas)

# for i in promedio_alumno_asignatura:
#     for j in asignaturas:


