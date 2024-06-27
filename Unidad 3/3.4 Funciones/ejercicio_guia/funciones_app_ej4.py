def calculadora_loca(operacion="suma_factorial",numeros=[1,2,3,4,5],debug="no"):
    try:

        if operacion.lower() == "suma":
            suma = 0
            for i in numeros:
                suma += i
            return suma
        
        elif operacion.lower() == "resta":
            resta = 0
            for i in range(len(numeros)):
                if i == 0:
                    resta += numeros[i]
                else:
                    resta -= numeros[i]
            return resta
        
        elif operacion.lower() == "division":
            division = 0
            for i in range(len(numeros)):
                if i == 0:
                    division += numeros[i]
                else:
                    division /= numeros[i]
            return division
        
        elif operacion.lower() == "multiplicacion":
            multiplicacion = 1
            for i in numeros:
                    multiplicacion *= i
            return multiplicacion
        
        elif operacion.lower() == "suma_factorial":
            suma_factorial = 0
            for i in numeros:
                factorial = 1
                for j in range(1,i+1):
                    factorial *= float(j)
                suma_factorial += factorial
            return suma_factorial
        
        elif operacion.lower() == "promedio":
            suma_promedio = 0
            for i in numeros:
                suma_promedio += i
            promedio = round(suma_promedio/len(numeros),2)
            return promedio
        
        else:
            print(f"Debe seleccionar una opción correcta. Favor referirse a la documentación!.")
        
    except TypeError :
        print(f"Recuerda que solo se aceptan numeros!!")
        if debug == "no":
            print("Terminando programa...")
        if debug == "si":
            return 1
    except Exception as e:
        print(f"Error! : {e}")
        print(f"El error fue : {e.with_traceback}")
        if debug == "no":
            print("Terminando programa...")
        if debug == "si":
            return 1