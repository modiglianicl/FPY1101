matriz = [
    [
    ["amarillo","rojo","naranja"],
    ["azul","lima","rojo"],
    ["cafe","brown","yellow"]
    ],
    [
    ["amarillo","rojo","naranja"],
    ["azul","lima","rojo"],
    ["cafe","brown","yellow"]
    ],
    [
    ["amarillo","rojo","naranja"],
    ["azul","lima","rojo"],
    ["cafe","brown","yellow"]
    ]
     ]

contador_amarillo = 0
contador_rojo = 0
contador_naranja = 0
contador_azul = 0
contador_lima = 0
contador_otros = 0
# No hice todos los colores , por que ya se entiende la gracia...
for i in range(len(matriz)):
    for j in range(len((matriz[i]))):
        for k in range(len(matriz[i][j])):
            print(f"{matriz[i][j][k]}")
            if matriz[i][j][k] == "amarillo":
                contador_amarillo += 1
            elif matriz[i][j][k] == "rojo":
                contador_rojo += 1
            elif matriz[i][j][k] == "naranja":
                contador_naranja += 1
            elif matriz[i][j][k] == "azul":
                contador_azul +=1
            elif matriz[i][j][k] == "lima":
                contador_lima +=1
            else:
                contador_otros +=1

print(f"---Resultado contadores (tiene que sumar 27, por que es 3x3x3)---")
print(f"Amarillos : {contador_amarillo}")
print(f"Rojos : {contador_rojo}")
print(f"Naranjas : {contador_naranja}")
print(f"Azules : {contador_azul}")
print(f"Limas : {contador_lima}")
print(f"Otros colores : {contador_otros}")
print(f"Total : {contador_amarillo + contador_rojo + contador_naranja + contador_azul + contador_lima + contador_otros}")