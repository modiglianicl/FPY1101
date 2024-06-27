# Funcion
# 3
def promediolista(lista_numeros):
    return round(sum(lista_numeros) / len(lista_numeros),2)


while True:
    try:
        numeros_raw = input("Ingrese una lista de numeros separados por una coma Ej :'1,2,3' o seran ignorados: ")
        numeros_separados = numeros_raw.split(',')
        numeros_parseados = []
        for i in numeros_separados:
            if i == "" or i.isalpha() or i in ("!","¿","?"):
                continue
            numeros_parseados.append(float(i))
        promedio = promediolista(numeros_parseados)
        print(f"El promedio final es {promedio}")
        break
    except ValueError : 
        print(f"Todos los elementos entregados deben ser un número!")
    except Exception as e :
        print(f"Error : {e}")
        print(f"{e.with_traceback}")