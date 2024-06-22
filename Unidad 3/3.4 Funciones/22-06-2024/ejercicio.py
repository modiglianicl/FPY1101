# Objetivo del programa: Un programa funcional que, dada una lista de números
# ingresada por el usuario, identifica y muestra los números pares e impares de
# manera clara y organizada

## Funciones ##
def preguntar_lista():
    todos_enteros = False
    while todos_enteros == False:
        numeros = (input("Ingrese una cantidad de numeros separados por una ',' : "))
        lista_numeros = numeros.split(',')
        lista_numeros_int = []
        for i in lista_numeros:
            try:
                lista_numeros_int.append(int(i))
                todos_enteros = True
            except ValueError:
                todos_enteros = False
        if todos_enteros:
            return lista_numeros_int
        else:
            print(f"Todos los valores deben ser números enteros! Intenta denuevo")

            

def chequeador_pares(lista_numeros):
    lista_pares = []
    lista_impares = []
    try:
        for i in lista_numeros:
            if int(i) % 2 == 0:
                lista_pares.append(int(i))
            else:
                lista_impares.append(int(i))
    except ValueError:
        print(f"Los valores otorgados deben ser numeros!")
    except Exception as e:
        print(f"Error {e}: {e.with_traceback}")
    return lista_pares,lista_impares

## Fin Funciones ##

lista_numeros = preguntar_lista()

pares,impares = chequeador_pares(lista_numeros)

if len(pares) > 0:
    print(f"Pares  : {pares}")
if len(impares) > 0:
    print(f"Impares : {impares}")