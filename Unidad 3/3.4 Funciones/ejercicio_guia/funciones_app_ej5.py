def hola():
    return "hola"

def registrar_usuario():
    nombre = input("Porfavor ingrese su nombre : ")
    rut = input("Porfavor ingrese su rut : ")
    direccion = input("Porfavor ingrese su dirección de domicilio : ")
    data_usuario = {
        "nombre" : nombre,
        "rut" : rut,
        "direccion" : direccion,
        "servicios" : {
            "Agua" : None,
            "Gas" : None,
            "Luz" : None,
            "Internet" : None,
            "Telefono" : None
        }
    }
# Info Agua
    while True:
        print("Seleccione su proveedor de Agua")
        print("1.- Esval")
        print("2.- Aguas Andina")
        try:
            opcion_agua = int(input("Introduzca el número que corresponda a su servicio de agua : "))
            if opcion_agua == 1:
                data_usuario["servicios"]["Agua"] = "Esval"
                break
            elif opcion_agua == 2:
                data_usuario["servicios"]["Agua"] = "Aguas Andina"
                break
            else:
                print(f"Debe ser una opción válida! (1 o 2)")
        except Exception as e:
            print(f"Debe ser una opción válida! (1 o 2)")
# Info Gas
    while True:
        print("Seleccione su proveedor de Gas")
        print("1.- Lipigas")
        print("2.- Gasco")
        print("3.- Abastible")
        try:
            opcion_gas = int(input("Introduzca el número que corresponda a su servicio de gas : "))
            if opcion_gas == 1:
                data_usuario["servicios"]["Gas"] = "Lipigas"
                break
            elif opcion_gas == 2:
                data_usuario["servicios"]["Gas"] = "Gasco"
                break
            elif opcion_gas == 3:
                data_usuario["servicios"]["Gas"] = "Abastible"
                break
            else:
                print(f"Debe ser una opción válida! (1 al 3)")
        except Exception as e:
            print(f"Debe seleccionar correctamente con un número! (1 al 3)")   

# Info Luz
    while True:
        print("Seleccione su proveedor de Luz")
        print("1.- CGE")
        print("2.- Colbun")
        print("3.- Chilquinta")
        print("4.- Chilectra")
        try:
            opcion_luz = int(input("Introduzca el número que corresponda a su servicio de gas : "))
            if opcion_luz == 1:
                data_usuario["servicios"]["Luz"] = "CGE"
                break
            elif opcion_luz == 2:
                data_usuario["servicios"]["Luz"] = "Colbun"
                break
            elif opcion_luz == 3:
                data_usuario["servicios"]["Luz"] = "Chilquinta"
                break
            elif opcion_luz == 4:
                data_usuario["servicios"]["Luz"] = "Chilectra"
                break
            else:
                print(f"Debe ser una opción válida! (1 al 4)")
        except Exception as e:
            print(f"Debe seleccionar correctamente con un número! (1 al 4)")           
# Info Internet
    while True:
        print("Seleccione su proveedor de Internet")
        print("1.- VTR")
        print("2.- Movistar")
        print("3.- Entel")
        try:
            opcion_internet = int(input("Introduzca el número que corresponda a su servicio de gas : "))
            if opcion_internet == 1:
                data_usuario["servicios"]["Internet"] = "VTR"
                break
            elif opcion_internet == 2:
                data_usuario["servicios"]["Internet"] = "Movistar"
                break
            elif opcion_internet == 3:
                data_usuario["servicios"]["Internet"] = "Entel"
                break
            else:
                print(f"Debe ser una opción válida! (1 al 3)")
        except Exception as e:
            print(f"Debe ser una opción válida! (1 al 3)")         
# Info Teléfono
    while True:
        print("Seleccione su proveedor de Télefono")
        print("1.- Entel")
        print("2.- WOM")
        print("3.- Movistar")
        print("4.- Claro")
        try:
            opcion_telefono = int(input("Introduzca el número que corresponda a su servicio de gas : "))
            if opcion_telefono == 1:
                data_usuario["servicios"]["Telefono"] = "Entel"
                break
            elif opcion_telefono == 2:
                data_usuario["servicios"]["Telefono"] = "WOM"
                break
            elif opcion_telefono == 3:
                data_usuario["servicios"]["Telefono"] = "Movistar"
                break
            elif opcion_telefono == 4:
                data_usuario["servicios"]["Telefono"] = "Claro"
                break
            else:
                print(f"Debe ser una opción válida! (1 al 4)")
        except Exception as e:
            print(f"Debe seleccionar correctamente con un número! (1 al 4)")
    # Return            
    return data_usuario
