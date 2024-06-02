bus = [[(j+1+4*i) for j in range(4)] for i in range(10)]


for i in range(len(bus)):
    for j in range(len(bus[i])):
        if j == 1:
            if bus[i][j] < 10:
                print(f" ",end="")
            print(f"{bus[i][j]}",end="     | |     ")
        elif j == 3:
            if bus[i][j] < 10:
                print(f" ",end="")
            print(f"{bus[i][j]}")
        else:
            if bus[i][j] < 10:
                print(f" ",end="")
            print(f"{bus[i][j]}",end="  ")

print(f"--- Sin comprension de listas ---")
# Sin comprension de listas

bus_fome = []

## Creamos las 10 filas
for i in range(10): 
    bus_fome.append([])

## Creamos las 4 columnas
for i in range(len(bus_fome)):
    for j in range(4):
        bus_fome[i].append((j+1)+(4*i)) # Parte en 1, y termina en 40

for i in range(len(bus_fome)):
    for j in range(len(bus[i])):
        if j == 1:
            if bus_fome[i][j] < 10:
                print(f" ",end="")
            print(f"{bus_fome[i][j]}",end="     | |     ")
        elif j == 3:
            if bus_fome[i][j] < 10:
                print(f" ",end="")
            print(f"{bus_fome[i][j]}")
        else:
            if bus_fome[i][j] < 10:
                print(f" ",end="")
            print(f"{bus_fome[i][j]}",end="  ")