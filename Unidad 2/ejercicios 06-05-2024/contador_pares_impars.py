# Contador impares y pares
contador_par = 0
contador_impar = 0

for i in range(10457):
    try:
        if i % 2 == 0:
            contador_par += 1
        elif i % 2 !=0:
            contador_impar +=1
    except Exception as e:
        print(f"Algo ocurrio... {e.with_traceback}")

print(f"Cantidad de pares : {contador_par}\n Cantidad de impares : {contador_impar}")