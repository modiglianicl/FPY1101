lista = [[0,0,0,0],
         [0,0,0,0],
         [0,0,0,0]
         ]

for i in range(len(lista)):
    for j in range(len(lista[i])):
        numero = int(input(f"Ingrese un numero para el indice {i},{j} : "))
        lista[i][j] = numero


for i in range(len(lista)):
    for j in range(len(lista[i])):
        if j == len(lista[i])-1:
            print(f"{lista[i][j]}")
        else:
            print(f"{lista[i][j]}",end="    ",)
