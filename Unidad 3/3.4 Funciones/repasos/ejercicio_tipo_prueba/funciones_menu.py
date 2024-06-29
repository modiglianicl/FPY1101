def menu_principal():
    print(f"1.- Obtener mejor alumno por asignatura")
    print(f"2.- Obtener el mejor alumno por año")
    print(f"3.- Obtener la asignatura de cada año con mejor asistencia")
    print(f"4.- Salir")


def opcion_uno(asignaturas,mejores_promedios_asignaturas):
    print(f"Las asignaturas disponibles son las siguientes : ")
    for i in range(len(asignaturas)):
        print(f"{i+1}.- {asignaturas[i]}")
    opcion_asignatura = int(input("Seleccione su asignatura : "))-1
    if opcion_asignatura in (range(0,len(asignaturas))):
        asignatura_seleccionada = asignaturas[opcion_asignatura]
        print(f"****** En la asignatura {asignatura_seleccionada} ******")
        for i in range(len(mejores_promedios_asignaturas)):
            if asignatura_seleccionada in mejores_promedios_asignaturas[i]:
                print(f"La mejor nota es un {mejores_promedios_asignaturas[i][asignatura_seleccionada]['mejor_nota']}")
                print(f"Que pertenece al alumno de rut {mejores_promedios_asignaturas[i][asignatura_seleccionada]['rut_alumno']}")
                print(f"************************************************")
    else:       
        print(f"Selecciona una opción valida!")

def opcion_dos(asistencia_anios,mejores_promedios_anio):
    print(f"Selecciona el año que quieras ver : ")
    for i in range(len(asistencia_anios.keys())):
        print(f"{i+1}.- {list(asistencia_anios.keys())[i]}")
    opcion_anio = int(input("Selecciona que año : ")) -1
    largo_opciones = len(list(asistencia_anios.keys()))
    if opcion_anio in range(0,largo_opciones):
        anio_seleccionado = list(asistencia_anios.keys())[opcion_anio]
        for anio in mejores_promedios_anio:
            if anio_seleccionado in anio:
                print(f"*** Datos {anio_seleccionado} ***")
                mejor_nota = anio[anio_seleccionado]['mejor_nota']
                mejor_alumno = anio[anio_seleccionado]['rut_alumno']
                print(f"El mejor alumno es el rut {mejor_alumno} con la nota {mejor_nota}")
    else :
        print("Debe de seleccionar una opción valida!")

def opcion_tres(asistencia_anios):
    print(f"Selecciona el año de la siguiente lista : ")
    for i in range(len(asistencia_anios.keys())):
        print(f"{i+1}.-{list(asistencia_anios.keys())[i]}")
    opcion_anio = int(input("Selecciona que anio : ")) - 1
    largo_opciones = len(list(asistencia_anios.keys()))
    mejor_asistencia = 0.0
    mejor_asignatura = ""
    if opcion_anio in (range(0,largo_opciones)):
        anio_seleccionado = list(asistencia_anios.keys())[opcion_anio]
        datos_anio = asistencia_anios[anio_seleccionado]
        largo_anio_seleccionado = len(list(datos_anio.keys()))
        asignaturas_anio = list(datos_anio.keys())
        print(f"*** Información asistencia {anio_seleccionado} ***")
        for i in range(0,largo_anio_seleccionado):
            asignatura = asignaturas_anio[i]
            asistencia_asignatura = []
            for i in datos_anio[asignatura]:
                asistencia_asignatura.append(int(i))
            promedio_asignatura = round(sum(asistencia_asignatura) / len(asistencia_asignatura),2)
            if promedio_asignatura > mejor_asistencia :
                mejor_asistencia = promedio_asignatura
                mejor_asignatura = asignatura
            print(f"{asignatura} : {promedio_asignatura}")
        print(f"*** Información mejor asistencia {anio_seleccionado} ***")
        print(f"Asignatura : {mejor_asignatura}; Promedio : {mejor_asistencia}")
    else:
        print(f"Debe de elegir una opción válida!")