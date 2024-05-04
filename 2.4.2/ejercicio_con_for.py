try:
    bultos = int(input("Cuantos bultos? \n"))
except ValueError:
    print("El valor debe ser un número!")
pesos_bultos = []
precio_bultos_livianos = 1000
precio_bultos_normales = 2000
bultos_livianos = 0
bultos_normales = 0

for i in range(bultos):
    try:
        bulto_input = int(input(f"Cuanto pesa (kg) el bulto n°{i+1}? \n"))
        pesos_bultos.append(bulto_input)
        if bulto_input < 20:
            bultos_livianos += 1
        else:
            bultos_normales +=1
    except ValueError:
        print("El peso debe ser un numero!")
        break

print(f"Hay {bultos_livianos} bultos livianos y {bultos_normales} bultos normales.")
valor_total = (bultos_livianos * precio_bultos_livianos) + (bultos_normales*precio_bultos_normales)
print(f"El valor total por los bultos es ", f"${valor_total:,}".replace(',','.'))