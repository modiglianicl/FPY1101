#Crear agenda telefonica donde la estructura del diccionario debe ser la siguiente:
#
#{
#    "nombre":{
#        "telefono" : string,
#        "email" : string,
#        "direccion" : string
#    }
#
#}

agenda_telefonica = []

while True:
    # Pidiendo datos
    nombre = input("Cual es su nombre : ")
    telefono = input("ingrese su telefono, me da lo mismo el largo : ")
    email = input("ingrese su correo (bien porfavor) : ")
    direccion = input("Ingrese su dirección : ")
    try:
        estadoUsuario = bool(int(input("Estado usuario (Habilitado = 1 / No Habilitado = 0) : ")))
    except ValueError:
        print(f"El valor del estado debe ser 1 o 0.")
    # Creando el objeto/diccionario
    datosUsuario = { nombre : {
        "telefono" : telefono,
        "email" : email,
        "direccion" : direccion,
        "estado" : estadoUsuario
    }}
    # Apendamos el diccionario a la lista
    agenda_telefonica.append(datosUsuario)
    # Pregunamos si queremos agregar mas usuarios
    continuarDatos = int(input("Desea continuar ? : 1.Si 2.No "))
    if continuarDatos == 2:
        break

# Imprimimos cada elemento de la lista
for i in range(len(agenda_telefonica)):
    print(agenda_telefonica[i])

