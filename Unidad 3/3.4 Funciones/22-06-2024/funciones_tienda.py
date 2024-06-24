# Función que agrega productos...
def agregar_producto(nuevo_producto,lista_productos):
    sku_producto = nuevo_producto['sku']
    registrable = False
    for i in lista_productos:
        if i['sku'] == int(sku_producto):
            registrable = False
        else:
            registrable = True
    if registrable:
        lista_productos.append(nuevo_producto)
        print("Ese SKU ya se encuentra registrado")

# Función que valida si existe el SKU y devuelve su indice (La usaré solo en actualizar y eliminar)
def validar_sku(sku,lista_productos):
    existe = False
    indice_detectado = None
    for i in range(len(lista_productos)):
        if lista_productos[i]['sku'] == sku:
            existe = True
            indice_detectado = i
    
    return existe,indice_detectado

# Función que permite actualizar cualquier elemento del producto
def actualizar_producto(sku_producto,lista_productos):
    # Llamos la funcion que valida si existe el SKU...
    existe_sku,indice = validar_sku(sku_producto,lista_productos)
    if existe_sku:
        print(f"**********El SKU Existe. Elija que valor quiere editar del producto**********")
        variables_producto = list(lista_productos[indice].keys())
        for i in range(len(variables_producto)):
            if i == 3:
                continue
            print(f"{i+1}.- {list(lista_productos[indice].keys())[i]}")
        variable_actualizar = int(input("Indique su selección : ")) - 1
        print(f"Usted selecciono {variables_producto[variable_actualizar]}")
        # Dependiendo si es int o str, le asignamos distintos inputs...
        direccion_editar = lista_productos[indice][variables_producto[variable_actualizar]]
        if type(direccion_editar) is int:
           lista_productos[indice][variables_producto[variable_actualizar]] = int(input("Asignele un nuevo valor (int): "))
        elif type(direccion_editar) is str:
            lista_productos[indice][variables_producto[variable_actualizar]] = input("Asignele un nuevo valor (str) : ")
    else:
        print(f"Ese SKU no existe en nuestros inventarios!")
    return None

def eliminar_producto(sku_producto,lista_productos):
    existe_sku,indice = validar_sku(sku_producto,lista_productos)
    if existe_sku:
        while True:
            confirmar_del = input("Esta seguro que desea borrar este producto ? (si/no) : ").lower()
            if confirmar_del == "no":
                print("No se eliminará este SKU, volviendo al menu")
                break
            if confirmar_del == "si":
                print("Procediendo a eliminar...")
                del lista_productos[indice]
                break
            else:
                print(f"Debe elegir si o no!")
    else:
        print("Ese SKU no existe!")
    return None

def nombre_nueva_funcion(holis):
    # Esta funcion la traeremos desde la rama development al main con un pull request
    print(f"{holis.upper()}")
    return "AYO"

