palabras = ["Hola","holis","arbol",
            "murcielago","panda","perro",
            "olores","negro","asdsadsadsa",
            "murciegalookgoskgofskgofskodkfokfoakf",
            "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"]
cantidad_vocales = 0
cantidad_consonantes = 0

for palabra in palabras:
    for i in palabra:
        if i in "aeiou":
            cantidad_vocales +=1
        else:
            cantidad_consonantes +=1

print(f"Cantidad de vocales : {cantidad_vocales} \n Cantidad de consonantes : {cantidad_consonantes}")
