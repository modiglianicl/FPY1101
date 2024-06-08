def esPrimo(listaNumeros):
    if len(listaNumeros) >= 2:
        conjuntoPrimos = set()
        for i in listaNumeros:
            divisoresCero = 0
            if i == 0:
                continue
            else:
                for j in listaNumeros:
                    if j == 0:
                        continue
                    elif i % j == 0:
                        divisoresCero +=1
                    else:
                        continue
            if divisoresCero == 2:
                conjuntoPrimos.add(i)
            else:
                continue
        if len(conjuntoPrimos) == 0:
            print(f"No hay primos en ese rango!")
            print(conjuntoPrimos)
        else:
            print(conjuntoPrimos)
    else:
        print(f"La lista debe tener al menos 2 numeros")

esPrimo(range(50,100))