# Librerias

import math



# Variables precios (En un array, index 0 es litros, index 1 es el precio en USD, index 2 cantidad de cada botella)

botellaEu = [float(750/1000.0), 1.5, 0]

botellaAsia = [float(700/1000), 0.9, 0]

botellaOceania = [float(850/1000), 2.3, 0]

tankTainer = [float(12000), 3500.0, 0]

cantidadLitros = 0

valorTotal = 0



# Pedimos datos del cotizante



while True:

  try:

    nombreReceptor = input("Ingrese su nombre.\n")

    fonoContacto = input("Ingrese un telefono de contacto.\n")

    continenteDestino = input("Ingrese el continente de destino.\n")

    break

  except ValueError as e:

    print(f"Error, favor re ingresar los datos : {e.with_traceback}")



# Realizacion cotizacion

    

while True:

  print(f"Porfavor elija que desea comprar")

  print(f"1.- Botella Europa (750 ml) @ USD$1.5")

  print(f"2.- Botella Asia (700 ml) @ USD$0.9")

  print(f"3.- Botella Oceanía (850ml) @ USD$2.3")

  print(f"4.- Terminar Cotización")

  try:

    compraRealizada = int(input(""))

    if compraRealizada == 1:

      while True:

        try:

          n_botellas = int(input("Cuantsa botellas de Europa desea comprar?\n"))

          if n_botellas > 0:

            cantidadLitros += botellaEu[0] * n_botellas

            botellaEu[2] += n_botellas

            valorTotal += botellaEu[1] * n_botellas

            break

          else:

            print(f"Debe comprar al menos una botella...")

            print(f"Volviendo al menú de productos.")

            break

        except Exception as e:

          print(f"Debe ingresar un numero, volviendo al menu de productos. Error : {e.with_traceback}")

          break

    elif compraRealizada == 2:

      while True:

        try:

          n_botellas = int(input("Cuantas botellas de Asia desea comprar?\n"))

          if n_botellas > 0:

            cantidadLitros += botellaAsia[0] * n_botellas

            botellaAsia[2] += n_botellas

            valorTotal += botellaAsia[1] * n_botellas

            break

          else:

            print(f"Debe comprar al menos una botella...")

            print(f"Volviendo al menú de productos.")

            break

        except Exception as e:

          print(f"Debe ingresar un numero, volviendo al menú de productos. Error : {e.with_traceback}")

          break



    elif compraRealizada == 3:

      while True:

        try:

          n_botellas = int(input("Cuantas botellas de Oceanía desea comprar?\n"))

          if n_botellas > 0:

            cantidadLitros += botellaOceania[0] * n_botellas

            botellaOceania[2] += n_botellas

            valorTotal += botellaOceania[1] * n_botellas

            

            break

          else:

            print(f"Debe comprar al menos una botella...")

            print(f"Volviendo al menú de productos.")

            break

        except Exception as e:

          print(f"Debe ingresar un numero, volviendo al menú de productos. Error : {e.with_traceback}")

          break

    elif compraRealizada == 4:

      print(f"Salir...")

      break

    else:

      print(f"Debe seleccionar entre 1 y 3")

  except ValueError as e:

    print(f"Error, debe de ingresar un número entre 1 y 3. [Debug] Error : {e.with_traceback}")



# Logica cantidad tanktainers

nTankTainers = math.ceil(cantidadLitros / 12000)

costeTankTainers = nTankTainers * 3500





# Cuando termina se muetra info cotizante y el total.

print(f"----- DATOS COTIZANTE -----:")

print(f"Nombre : {nombreReceptor}")

print(f"Telefono : {fonoContacto}")

print(f"Continente Destino : {continenteDestino}")

print(f"----- DATOS COTIZACION -----:")

print(f"Tanktainer : {nTankTainers}")

print(f"Valor Transporte : USD${round(costeTankTainers,2):,}")

print(f"Detalle Botellas")

if botellaEu[2] > 0:

  print(f"{botellaEu[2]} botellas x USD$1.5 => Total costo botellas USD${round((botellaEu[2] * botellaEu[1]),2):,}")

else:

  print(f"")

if botellaAsia[2] > 0:

  print(f"{botellaAsia[2]} botellas x USD$0.9 => Total costo botellas USD${round((botellaAsia[2] * botellaAsia[1]),2):,}")

if botellaOceania[2] > 0:

  print(f"{botellaOceania[2]} botellas x USD$2.3 => Total costo botellas USD${round((botellaOceania[2] * botellaOceania[1]),2):,}")

print(f"Cantidad de Litros : {round(cantidadLitros,2)} litros.")

print(f"Costo total exportacion : USD${(round(valorTotal + costeTankTainers,2)):,}")