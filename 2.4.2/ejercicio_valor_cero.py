try:
    numerador = float(input("Ingrese el numerador : "))
    divisor = float(input("Ingrese el divisor (que no sea cero porfavor) : "))
    if divisor == 0:
        raise ZeroDivisionError("No se puede dividir por 0!")
    
    resultado = numerador/divisor
    print(f"El resultado es {resultado}")

except ValueError as ve:
    print(f"Error {ve}")
finally:
    print("Programa termino.")
