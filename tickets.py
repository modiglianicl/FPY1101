# Precios tickets
ticket_adulto = 5000
ticket_amayor = 2500
ticket_nino = 2000

# Solicitando e inicializando datos datos
nombre_usuario = input("Ingresa tu nombre : \n")
edad_usuario = int(input("Ingresa tu edad : \n"))
total_compra = 0

# Logica
    ## Si usuario es mayor a 18 preguntar cuantos tickets
if edad_usuario >= 60:
    cantidad = int(input("Cuantos tickets adulto mayor desea comprar? : \n"))
    total_compra = cantidad * ticket_amayor
    print(f"Estimado {nombre_usuario}", f"el total a pagar es : ${total_compra:,}".replace(',','.')) ## Formateo separador de miles con coma, despues reemplazo comas por puntos con ".replace(',','.')"
elif edad_usuario >= 18:
    cantidad = int(input("Cuantos tickets adultos desea comprar? : \n"))
    total_compra = cantidad * ticket_adulto
    print(f"Estimado {nombre_usuario}", f"el total a pagar es : ${total_compra:,}".replace(',','.'))
elif edad_usuario < 18:
    cantidad = int(input("Cuantos tickets de niño desea comprar? : \n"))
    total_compra = cantidad * ticket_nino
    print(f"Estimado {nombre_usuario}", f"el total a pagar es : ${total_compra:,}".replace(',','.'))

