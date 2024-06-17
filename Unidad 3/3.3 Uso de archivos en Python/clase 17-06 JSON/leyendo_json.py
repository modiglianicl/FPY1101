import json

lista_diccionario = []
with open('archivo.json','r') as archivo:
    datos_leidos = json.load(archivo)
    for i in datos_leidos:
        lista_diccionario.append(i)


print(lista_diccionario)