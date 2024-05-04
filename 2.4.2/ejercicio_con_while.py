## Ojo defini mi propia clasificacion de que es liviano y que es normal, el ejercicio no dice que es liviano y que es un bulto normal
try:
    bultos = int(input("Cuantos bultos? \n"))
except ValueError:
    print("El valor debe ser un número!, terminando programa")
    quit()

nroBulto = 0 ## Contador que me permite el control de donde vamos.
pesos_bultos = []
precio_bultos_livianos = 1000
precio_bultos_normales = 2000
bultos_livianos = 0
bultos_normales = 0

while nroBulto < bultos:
    try:
        bulto_input = int(input(f"Cuanto pesa (kg) el bulto n°{nroBulto+1}? \n"))
        pesos_bultos.append(bulto_input)
        if bulto_input < 20:
            bultos_livianos += 1
        else:
            bultos_normales +=1
        nroBulto += 1
    except ValueError:
        print("El peso debe ser un numero!, intenta denuevo!") ## No sumamos a nroBulto para que el usuario intente denuevo en el mismo bulto...

# Mostrando cada peso
print(f"Los pesos de todos los bultos son :")
for i in range(0,len(pesos_bultos)):
    print(f"{i+1}.- {pesos_bultos[i]} kg.")
# Resumen
print(f"Hay {bultos_livianos} bultos livianos y {bultos_normales} bultos normales.")
# Valor final
valor_total = (bultos_livianos * precio_bultos_livianos) + (bultos_normales*precio_bultos_normales)
print(f"El valor total por los bultos es de", f"${valor_total:,}".replace(',','.'))