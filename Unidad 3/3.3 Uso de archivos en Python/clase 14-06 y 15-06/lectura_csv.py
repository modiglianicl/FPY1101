import csv

lista_de_datos = []



with open('estudiantes.csv', 'r', newline='', encoding='utf-8') as archivo:
    lista_de_datos = csv.reader(archivo)
    contador = 0
    suma = 0
    promedio_alto = 0
    for fila in lista_de_datos:
        if (fila[6] == 'asistencia_final'):
            continue
        else:
            contador += 1
            suma += int(fila[6])
            promedio_alumno = (float(fila[3]) + float(fila[4]) + float(fila[5]))/3
            if promedio_alumno > promedio_alto:
                print(fila[0], fila[1], promedio_alumno)
                promedio_alto = promedio_alumno
                
    print(contador)
    print(suma)
    print(suma/contador)
    print(promedio_alto)