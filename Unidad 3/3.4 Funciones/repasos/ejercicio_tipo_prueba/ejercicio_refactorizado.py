# Ejercicio tipo prueba, refactorizado con funciones

# Librerias
import funciones_analisis as fn
import funciones_menu as fm
import os

lista_diccionarios = []

nombre_archivo = f"{os.getcwd()}\\alumnos_detallado.csv"
lista_diccionarios = fn.csv_to_json(nombre_archivo)

##### Mejor alumno por asignatura ##### 

# Calculamos promedios de cada alumno por asignatura
promedio_alumno_asignatura = fn.promedios_por_asignatura(lista_diccionarios)
# Obtenemos asignaturas
asignaturas = fn.obtener_asignaturas(lista_diccionarios)
# Calculamos mejores promedios de cada asignatura
mejores_promedios_asignaturas = fn.max_promedio_asignatura(lista_diccionarios)
    
##### Mejor alumno por año ##### 

# Obteniendo los años que existen en el dataset
anios_dataset = fn.obtener_anios(lista_diccionarios)

# Obtenemos los mejores promedios por anio

mejores_promedios_anio = fn.mejores_promedios_anio(anios_dataset,promedio_alumno_asignatura)
    
##### Asignatura con mejor asistencia ##### 
    
# Diccionario con todos los años y dentro de este cada asignatura con su asistencia promedio (inicializados en 0)
    # Ojo, para probar , no lo hice como una lista, es un diccionario de diccionarios
    
asistencia_anios = fn.asignatura_mejor_asistencia(anios_dataset,asignaturas,lista_diccionarios)

## Menu ##

while True:
    try:
        fm.menu_principal()
        opcion = int(input("Ingrese su opción : "))
        if opcion == 1 :
            fm.opcion_uno(asignaturas,mejores_promedios_asignaturas)
        elif opcion == 2:
            fm.opcion_dos(asistencia_anios,mejores_promedios_anio)
        elif opcion == 3:
            fm.opcion_tres(asistencia_anios)
        elif opcion == 4:
            print(f"Terminando programa...")
            break
    except ValueError:
        print("Debe de usar un valor correcto!")
    except Exception as e:
        print(f"Algo ocurrió! : {e} , {e.with_traceback}")
