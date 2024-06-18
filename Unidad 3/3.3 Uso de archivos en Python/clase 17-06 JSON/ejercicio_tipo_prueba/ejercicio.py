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

##### Mejor alumno por asignatura ##### 

# Obteniendo asignaturas
asignaturas = []

for i in lista_diccionarios:
    asignaturas.append(i['asignatura'])
# Creamos conjunto para eliminar duplicados
asignaturas = set(asignaturas)
asignaturas = list(asignaturas)

# Calculamos promedios de cada alumno por asignatura
promedio_alumno_asignatura = []
for i in lista_diccionarios:
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
    
# Escribimos
with open('dicasignaturas.json','w',encoding='utf-8') as archivo:
     datos_1 = json.dump(mejores_promedios_asignaturas,archivo,ensure_ascii=False)

# Encontramos el maximo promedio para cada asignatura
for i in promedio_alumno_asignatura:
     for j in range(len(asignaturas)):
         if i['asignatura'] == asignaturas[j]:
             if i['promedio_alumno'] > mejores_promedios_asignaturas[j][asignaturas[j]]['mejor_nota']:
                 mejores_promedios_asignaturas[j][asignaturas[j]]['mejor_nota'] = i['promedio_alumno']
                 mejores_promedios_asignaturas[j][asignaturas[j]]['rut_alumno'] = i['rut']

with open('mejoresnotasporasignatura.json','w',encoding='utf-8') as archivo:
    datos_1 = json.dump(mejores_promedios_asignaturas,archivo,ensure_ascii=False)


##### Fin mejor alumno por asignatura ##### 
    
##### Mejor alumno por año ##### 

# Obteniendo los años que existen en el dataset
anios_dataset = []
for i in lista_diccionarios:
    anios_dataset.append(i['curso'])
anios_dataset = set(anios_dataset)
anios_dataset = list(anios_dataset)

##Construimos un diccionario con año como llave , mejor promedio y rut

mejores_promedios_anio = []

for i in anios_dataset:
    diccionario = {
        i : {
            'mejor_nota' : 0.0,
            'rut_alumno' : ""
        }
    }
    mejores_promedios_anio.append(diccionario)

for i in promedio_alumno_asignatura:
    for j in range(len(anios_dataset)):
        if i['curso'] == anios_dataset[j]:
            if i['promedio_alumno'] > mejores_promedios_anio[j][anios_dataset[j]]['mejor_nota']:
                mejores_promedios_anio[j][anios_dataset[j]]['mejor_nota'] = i['promedio_alumno']
                mejores_promedios_anio[j][anios_dataset[j]]['rut_alumno'] = i['rut']

with open('mejoralumnoporanio.json','w',encoding='utf-8') as archivo:
    datos_1 = json.dump(mejores_promedios_anio,archivo,ensure_ascii=False)

##### Fin Mejor alumno por año ##### 
    
##### Asignatura con mejor asistencia ##### 
    
# Diccionario con todos los años y dentro de este cada asignatura con su asistencia promedio (inicializados en 0)
    # Ojo, para probar , no lo hice como una lista, es un diccionario de diccionarios
    
asistencia_anios = {}

for i in anios_dataset:
    asistencia_anios[i] = {}
    for j in asignaturas:
        asignatura = str(j)
        asistencia_anios[i][asignatura] = []

# Agregandos asistencias por año por asignatura
for i in lista_diccionarios:
    anio = i['curso']
    asignatura = i['asignatura']
    asistencia = i['asistencia']
    asistencia_anios[anio][asignatura].append(int(asistencia))

# Eliminamos las asignaturas que no corresponden a un año
for i in anios_dataset:
    for j in asignaturas:
        if len(asistencia_anios[i][j]) < 1:
            del asistencia_anios[i][j]

# with open('diccionario_asistencia_anios.json','w',encoding='utf-8') as archivo:
#     data_1 = json.dump(asistencia_anios,archivo,ensure_ascii=False)
#### Fin Asignatura con mejor asistencia ##### 
    

## Menu ##

while True:
    print(f"1.- Obtener mejor alumno por asignatura")
    print(f"2.- Obtener el mejor alumno por año")
    print(f"3.- Obtener la asignatura de cada año con mejor asistencia")
    print(f"4.- Salir")
    opcion = int(input("Ingrese su opción : "))

    if opcion == 1 :
        print(f"Las asignaturas disponibles son las siguientes : ")
        for i in range(len(asignaturas)):
            print(f"{i+1}.- {asignaturas[i]}")
        opcion_asignatura = int(input("Seleccione su asignatura : "))
        if opcion_asignatura in (range(0,len(asignaturas))):
            asignatura_seleccionada = asignaturas[opcion_asignatura-1]
            print(f"En la asignatura {asignatura_seleccionada}")
            for i in range(len(mejores_promedios_asignaturas)):
                if asignatura_seleccionada in mejores_promedios_asignaturas[i]:
                    print(f"La mejor nota en {list(mejores_promedios_asignaturas[i].keys())[0]} Es un {mejores_promedios_asignaturas[i][asignatura_seleccionada]['mejor_nota']}")
                    print(f"Que pertenece al alumno de rut {mejores_promedios_asignaturas[i][asignatura_seleccionada]['rut_alumno']}")
        else:
            print(f"Selecciona una opción valida!")
    elif opcion == 2:
        print(f"Selecciona el año de la siguiente lista : ")
        for i in range(len(anios_dataset)):
            print(f"{i+1}.-{anios_dataset[i]}")
        opcion_anio = int(input("Selecciona que anio : "))
        if opcion_anio in (range(0,len(anios_dataset))):
            print(f"Aca va el analisis")
    


    elif opcion == 4:
        print(f"Terminando programa...")
        break
