import csv
import json

lista_json = []
nombre_csv = 'estudiantes.csv'
# Abre el archivo, w es escritura
try:
    with open(nombre_csv,'r',newline='',encoding='utf-8') as archivo : 
        datos = csv.reader(archivo)
        for i in datos:
            datos_dict = {}
            datos_dict["notas"] = {}
            datos_dict["nombre"] = i[0]
            datos_dict["apellido"] = i[1]
            datos_dict["asignatura"] = i[2]
            datos_dict["notas"]["nota1"] = i[3]
            datos_dict["notas"]["nota2"] = i[4]
            datos_dict["notas"]["nota3"] = i[5]
            datos_dict["asistencia_final"] = i[6]
            lista_json.append(datos_dict)
        for i in lista_json:
            print(i)

    with open('archivo.json','w',encoding='utf-8') as archivo:
        datos_1 = json.dump(lista_json,archivo,ensure_ascii=False)

except FileNotFoundError as e:
    print(f"El archivo no existe.")
except json.JSONDecodeError: # En caso de que el json no tenga formato correcto (Al escribir o leer.)
    print(f"Error en {datos}")
except Exception as e:
    print(f"Error : {e}")