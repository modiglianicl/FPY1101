import random

cara = []

colores = ["Rojo",
           "Amarillo",
           "Verde",
           "Naranja",
           "Blanco"]

cant_amarillo = 0
cant_rojo = 0
cant_verde = 0
cant_naranja = 0
cant_blanco = 0

for i in range(3):
    fila = []
    for j in range(3):
        columna = []
        for k in range(3):
            color = colores[random.randint(0,4)]
            if color.lower() == "amarillo" :
                cant_amarillo += 1
            elif color.lower() == "rojo" : 
                cant_rojo +=1
            elif color.lower() == "verde" :
                cant_verde +=1
            elif color.lower() == "naranja" :
                cant_naranja +=1
            elif color.lower() == "blanco" :
                cant_blanco +=1
            
            columna.append(color)
        fila.append(columna)
    cara.append(fila)

print(cara)