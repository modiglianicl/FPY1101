palabras = ["Hola","holis","arbol",
            "murcielago","panda","perro",
            "olores","negro","asdsadsadsa",
            "murciegalookgoskgofskgofskodkfokfoakf",
            "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",222]
cantidad_vocales = 0
cantidad_consonantes = 0

for palabra in palabras:
    print(f"Revisando {palabra} la cual es {type(palabra)}")
    if isinstance(palabra,int) == False :
        for i in palabra:
            if i in "aeiou":
                cantidad_vocales +=1
            else:
                cantidad_consonantes +=1
    else:
        continue

print(f"Cantidad de vocales : {cantidad_vocales} \n Cantidad de consonantes : {cantidad_consonantes}")
