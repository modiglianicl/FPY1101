import csv
import json

def csv_to_json(nombre_archivo):
    lista_diccionarios = []

    with open(nombre_archivo,'r',encoding='utf-8') as archivo:
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
                'promedio' : round((float(i[5]) + float(i[6]) + float(i[7]))/3,2),
                'asistencia' : i[8]
            }
            lista_diccionarios.append(datos_dict)
    return lista_diccionarios

def obtener_asignaturas(lista_dict):
    asignaturas = []

    for i in lista_dict:
        asignaturas.append(i['asignatura'])
    asignaturas = set(asignaturas)
    asignaturas = list(asignaturas)
    return asignaturas  

# Funcion para sacar promedios de cada algumno por asignatuira
def promedios_por_asignatura(lista_dict):
    asignaturas = obtener_asignaturas(lista_dict)
    
    # Creamos conjunto para eliminar duplicados
    promedio_alumno_asignatura = []
    for i in lista_dict:
        for j in asignaturas:
            if i['asignatura'] == j:
                datos = {
                    'rut' : i['rut'],
                    'asignatura' : j,
                    'curso' : i['curso'],
                    'promedio_alumno' : round((float(i['notas']['nota1'])+
                                float(i['notas']['nota2'])+
                                float(i['notas']['nota3']))/3,2)
                }
                promedio_alumno_asignatura.append(datos)

    return promedio_alumno_asignatura

# Maximo promedio para cada asignatura

def max_promedio_asignatura(lista_dict):
# Obteniendo asignaturas
    asignaturas = obtener_asignaturas(lista_dict)

    # Calculamos promedios de cada alumno por asignatura
    promedio_alumno_asignatura = promedios_por_asignatura(lista_dict)

    # Inicializando cada asignatura con un 0.0
    mejores_promedios_asignaturas = []

    for i in asignaturas:
        diccionario = {
            i : {
                'mejor_nota' : 0.0,
                'rut_alumno' : ''
            },
        }
        mejores_promedios_asignaturas.append(diccionario)

    # Encontramos el maximo promedio para cada asignatura
    for i in promedio_alumno_asignatura:
        for j in range(len(asignaturas)):
            if i['asignatura'] == asignaturas[j]:
                if i['promedio_alumno'] > mejores_promedios_asignaturas[j][asignaturas[j]]['mejor_nota']:
                    mejores_promedios_asignaturas[j][asignaturas[j]]['mejor_nota'] = i['promedio_alumno']
                    mejores_promedios_asignaturas[j][asignaturas[j]]['rut_alumno'] = i['rut']  

    return mejores_promedios_asignaturas

def obtener_anios(lista_dict):
    anios_dataset = []
    for i in lista_dict:
        anios_dataset.append(i['curso'])
    anios_dataset = set(anios_dataset)
    anios_dataset = list(anios_dataset)  
    return anios_dataset

def mejores_promedios_anio(anios,promedios_alumnos_asignatura):
    anios_dataset = anios
    mejores_promedios_por_anio = []
    for i in anios_dataset:
        diccionario = {
            i : {
                'mejor_nota' : 0.0,
                'rut_alumno' : ""
            }
        }
        mejores_promedios_por_anio.append(diccionario)

    for i in promedios_alumnos_asignatura:
        for j in range(len(anios_dataset)):
            if i['curso'] == anios_dataset[j]:
                if i['promedio_alumno'] > mejores_promedios_por_anio[j][anios_dataset[j]]['mejor_nota']:
                    mejores_promedios_por_anio[j][anios_dataset[j]]['mejor_nota'] = i['promedio_alumno']
                    mejores_promedios_por_anio[j][anios_dataset[j]]['rut_alumno'] = i['rut']

    with open('mejoralumnoporanio.json','w',encoding='utf-8') as archivo:
        datos_1 = json.dump(mejores_promedios_por_anio,archivo,ensure_ascii=False)
    return mejores_promedios_por_anio

def asignatura_mejor_asistencia(anios,asignaturas,lista_dict):
    asistencia_anios = {}

    for i in anios:
        asistencia_anios[i] = {}
        for j in asignaturas:
            asignatura = str(j)
            asistencia_anios[i][asignatura] = []

    # Agregandos asistencias por año por asignatura
    for i in lista_dict:
        anio = i['curso']
        asignatura = i['asignatura']
        asistencia = i['asistencia']
        asistencia_anios[anio][asignatura].append(int(asistencia))

    # Eliminamos las asignaturas que no corresponden a un año
    for i in anios:
        for j in asignaturas:
            if len(asistencia_anios[i][j]) < 1:
                del asistencia_anios[i][j]

    with open('diccionario_asistencia_anios.json','w',encoding='utf-8') as archivo:
        data_1 = json.dump(asistencia_anios,archivo,ensure_ascii=False,indent=4)
    return asistencia_anios   
