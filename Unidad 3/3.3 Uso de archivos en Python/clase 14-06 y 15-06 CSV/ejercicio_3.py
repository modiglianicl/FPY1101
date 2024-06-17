import csv

# Lista de los datos raw
lista_datos = []

# Lista nueva en donde se guardan los nuevos datos modificados
lista_descarga = []

# Lee los datos, agrega todo a lista_datos sin filtrar
with open('estudiantes.csv', 'r', newline='', encoding='utf-8') as archivo:
    datos = csv.reader(archivo)
    for i in datos:
        lista_datos.append(i)

# Itera sobre los datos que guardo en lista_datos        
for fila in lista_datos:
    if fila[0] == 'nombre': # Está es importante, la primera fila usa su primer elemento para detectar si son las columnas (es decir, texto)
        lista_descarga.append(fila)
    else: # Si no son las columnas aplicamos la logica que queriamos
        promedio = round((float(fila[3]) + float(fila[4]) + float(fila[5]))/3,2)
        if promedio >= 4.0 and int(fila[6]) >= 60: # Apueba si el promedio es mayor o igual a 4.0 y la asistencia mayor o igual a 60
            estado = 'Aprobado'
        else: # Si no, reprueba
            estado = 'Reprobado'
        nueva_fila = [fila[0],fila[2],promedio,fila[6],estado] # Guardamos todos los datos que obtuvimos en una fila (en el mismo orden que las columnas) 0 = nombre , 2 = asignatura , promedio = promedio obtenido , 6 = asistencia , estado = estado
        lista_descarga.append(nueva_fila) # Apendamos cada fila en la lista de filas

# Escribimos todo en archivo 'descarga.csv'
with open('descarga.csv', 'w', newline='') as descarga:
    descarga_reader = csv.writer(descarga)
    
    descarga_reader.writerows(lista_descarga)