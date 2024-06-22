# Crear un menu en donde pueda agregar , actualizar , eliminar productos de una tienda. No puede tener el mismo SKU,
import funciones_tienda as fn
import json
import pathlib

productos = [
    {
        "nombre_producto" : "Coca-Cola",
        "precio" : 1990,
        "cantidad" : 60,
        "sku" : 1
    },
        {
        "nombre_producto" : "Galletas",
        "precio" : 600,
        "cantidad" : 400,
        "sku" : 2
    },
        {
        "nombre_producto" : "Papas Fritas",
        "precio" : 300,
        "cantidad" : 1000,
        "sku" : 3
    }

]

salir = False

while not salir:
    print("Sistema de Tienda")
    print("1.- Agregar Producto")
    print("2.- Actualizar Producto")
    print("3.- Eliminar Producto")
    print("4.- Ver lista de productos (JSON)")
    print("5.- Generar archivo JSON actualizado")
    print("6.- Salir")
    
    opcion = int(input("Selecciona la opción : "))
    # Opción Agregar Producto
    if opcion == 1:
        while True:
            try:
                # Solicitamos datos del producto nuevo
                nombre_producto = input("Ingrese nombre producto : ")
                precio_producto = int(input("Ingrese precio de producto : "))
                cantidad_producto = int(input("Ingrese cantidad  de producto : "))
                sku = int(input("Ingrese sku de producto : "))
                datos_producto_nuevo = {
                        "nombre_producto" : nombre_producto,
                        "precio" : precio_producto,
                        "cantidad" : cantidad_producto,
                        "sku" : sku
                }
                # Agregamos y volvemos al menú
                fn.agregar_producto(datos_producto_nuevo,productos)
                break
            except ValueError:
                print(f"Verifique que ingresó un dato válido.")
    # Fin Opción Agregar Producto
    
    # Opcion actualizar producto
    elif opcion == 2:
        try:
            sku_actualizar = int(input("Ingrese el SKU del producto a actualizar : "))
            fn.actualizar_producto(sku_actualizar,productos)
        except ValueError:
            print(f"Debe ingresar un valor correcto.")
    # Fin opcion actualizar producto

    # Opción eliminar Producto    
    elif opcion == 3:
        try:
            sku_eliminar = int(input("Ingrese el SKU del producto a eliminar : "))
            fn.eliminar_producto(sku_eliminar,productos)
        except ValueError:
            print(f"Debe ingresar un valor correcto.")
    # Fin eliminar producto
            
    # Opción mostrar productos
    elif opcion == 4:
        print(productos)
    # Fin mostrar productos
        
    # Opcion generar JSON
    elif opcion == 5:
        print(f"Generando archivo 'productos.json'...")
        with open('productos.json','w',encoding='utf-8') as jsonfile:
            json.dump(productos,jsonfile,ensure_ascii=False,indent=4)
    # Fin generar JSON
            
    elif opcion == 6:
        print(f"Terminando programa...")
        break