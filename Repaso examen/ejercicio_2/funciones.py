import csv

def leer_archivo(archivo):
    datos = []
    with open(archivo,'r',encoding='utf-8') as file:
        datos_raw = csv.reader(file)
        for i in datos_raw:
            datos.append(i)
    return datos

def contar_likes(interacciones):
    likes = 0
    for i in interacciones:
        if i[2] == "like":
            likes +=1
    return likes

def contar_comentarios(interacciones):
    comentarios = 0
    for i in interacciones:
        if i[2] == "comment":
            comentarios +=1
    return comentarios

def total_interacciones(interacciones):
    likes = contar_likes(interacciones)
    comentarios = contar_comentarios(interacciones)
    return likes + comentarios

def calcular_edad(fecha):
    anio_nacimiento = int(fecha[:4])
    edad = 2024 - anio_nacimiento
    return edad

def unir_datos(usuarios,interacciones,top=3):
    datos_full = usuarios[:]
    # Obtenemos la edad de cada usuario, ahora la tercera columna es su edad (como pide el ejercicio)
    saltar_fila = 0
    for i in datos_full:
        if saltar_fila == 0:
            saltar_fila +=1
            continue
        fecha_nacimiento = calcular_edad(i[2])
        i[2] = fecha_nacimiento
    # Editamos "columnas"
    datos_full[0] = ["id_usuario","nombre_usuario","edad","total_likes","total_comments","numero_interacciones","es_top_usuario"]
    # Contamos el total de likes por usuario likes = columna 4 , comentarios = 5 , interacciones = 6
    saltar_fila = 0
    for i in datos_full:
        if saltar_fila == 0:
            saltar_fila += 1
            continue
        i.append(0) # inicializamos likes
        i.append(0) # inicializamos comentarios
        i.append(0) # inicializamos numero interacciones
        i.append(False) # inicializamos si es top usuario
        for j in interacciones:
            if i[0] == j[0]:
                if j[2] == "like":
                        i[3] +=1
                elif j[2] == "comment":
                        i[4] +=1
        i[5] = i[3] + i[4]

    # Detectando si es top 3
    top_3_usuarios = []
    for i in range(top):
        maximo = 0
        usuario = ""
        saltar_fila_uno = 0
        for j in datos_full:
            if saltar_fila_uno == 0:
                saltar_fila_uno +=1
                continue
            if j[0] not in top_3_usuarios:
                if j[5] > maximo:
                    maximo = j[5]
                    usuario = j[0]
        top_3_usuarios.append(usuario)

    # Dandole True a los mejores 3 usuarios
    for i in datos_full:
        if i[0] in top_3_usuarios:
            i[6] = True
    
    print(f" top 3 usuarios : {top_3_usuarios}")
    return datos_full

def generar_csv(datos_full):
    with open('reporte_interacciones.csv','w',encoding='utf-8',newline='') as file:
        writer = csv.writer(file)
        writer.writerows(datos_full)
                
