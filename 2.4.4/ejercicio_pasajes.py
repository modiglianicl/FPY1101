# Cuantos pasajes venderemos
cantidad_pasajes = int(input("Cuantos pasajes se venderan? : "))
totalIngresos = 0
# Preguntamos valor de cada pasaje
for i in range(cantidad_pasajes):
    try:
        valor_pasaje = int(input(f"Cuanto vale el pasaje {i+1} ? : "))
        if isinstance(valor_pasaje,int):
            totalIngresos += valor_pasaje
    except ValueError:
        print("El valor debe ser un número!, terminando asistente de ventas.")
        break

if totalIngresos > 0:
    print(f"Total ingresos por {cantidad_pasajes} pasajes : ${totalIngresos:,}")
else:
    print(f"No se realizo ninguna venta.")