# Weas que necesito
lista_numeros = [4,2,5,5656,4343,11,44,55,77]
sumar_n = 0
suma = 0

# Pregunto n que no puede ser mayor al largo de la lsta
while True:
    try:
        sumar_n = int(input("Cuantos numeros quieres sumar"))
    except Exception as e:
        print(f"Algo ocurrio...{e.with_traceback}")
    if sumar_n > len(lista_numeros):
        print(f"No puede ser mayor a {len(lista_numeros)}")
        continue
    else:
        break

# Sumo lo que quiero
for i in range(sumar_n):
    suma += lista_numeros[i]

print(suma)