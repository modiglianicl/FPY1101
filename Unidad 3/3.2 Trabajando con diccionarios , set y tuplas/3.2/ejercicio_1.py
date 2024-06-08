texto = input("Ingrese un texto : ")
lista_palabras = texto.split()
diccionario_palabras = {}

for i in range(len(lista_palabras)):
    llaveIterada = lista_palabras[i].lower()
    if llaveIterada in diccionario_palabras:
        diccionario_palabras[llaveIterada] += 1
    else : 
        diccionario_palabras[llaveIterada] = 1
    

print(diccionario_palabras)