def esPrimo(listaNumeros):
    if len(listaNumeros) >= 1:
        conjuntoPrimos = set()
        for i in listaNumeros:
            divisoresCero = 0
            if i == 0:
                continue
            else:
                for j in range(1,i+1):
                    if j == 0:
                        continue
                    elif i % j == 0:
                        divisoresCero +=1
            if divisoresCero == 2:
                conjuntoPrimos.add(i)
                
        if len(conjuntoPrimos) == 0:
            print(f"No hay primos en ese rango!")
            print(conjuntoPrimos)
        else:
            print(conjuntoPrimos)
    else:
        print(f"La lista debe tener al menos 2 numeros")

esPrimo(range(1,26))