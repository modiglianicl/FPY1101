texto = input("Dame un texto : ")
lista_palabras = texto.split()
diccionario_palabras = {}

for i in range(len(lista_palabras)):
    palabraIterada = lista_palabras[i].lower()
    if palabraIterada in diccionario_palabras:
        diccionario_palabras[palabraIterada] += 1
    else:
        diccionario_palabras[palabraIterada] = 1

print(diccionario_palabras)
