# Creamos arreglo tridimensional
test = [[j for j in range(3)]for i in range(3)]


try : 
    for i in range(len(test)):
        try:
            print(f"lista indice n°{i}: {test[i]}")
        except Exception as e: # Si ocurre algun error.
            print("Algo pasó")
        for j in range(len(test[i])):
            try:
                print(test[i][j])
            except Exception as e: # Si ocurre algun error.
                print(f"Algo pasó")
except IndexError as e: # Se que lo mas probable es que haya error de indice
    print(f"Error {e.with_traceback} en el indice! {i}")

else:
    print("Todo ok!") # Se imprime si no hay error!
finally:
    print("Nose si todo ok , pero igual aparezco!") # Se imprime si o si!
