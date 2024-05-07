# Contador impares y pares
contador_par = 0
contador_impar = 0

for i in range(10457):
    if i % 2 == 0:
        contador_par += 1
    elif i % 2 !=0:
        contador_impar +=1

print(f"Cantidad de pares : {contador_par}\n Cantidad de impares : {contador_impar}")