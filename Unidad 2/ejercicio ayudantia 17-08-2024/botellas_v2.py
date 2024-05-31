europa_litros = 0.75
costo_europa = 1.5
asia_litros = 0.7
costo_asia = 0.9
oceania_litros = 0.85
costo_oceania = 2.3
tanktainer_litros = 12000
costo_tanktainer = 3500
valor_total = 0
total_litros = 0

#Nombre del receptor del producto (al menos debe tener 2 letras)
#Fono contacto (debe poseer entre 9 dígitos)
#Continente Destino
#Litros a exportar
print("Cotizacion transporte")

while True:
    try:
        while True:
            nombre = input("Ingrese nombre: ")
            print(nombre)

            if len(nombre) >= 2:
                break
            else:
                print("debe tener mas de 2 letras")

        while True:
            fono = int(input("ingrese fono: "))
            print(fono)
            if len(str(fono)) != 9:
                print(f"El telefono tiene que tener 9 digitos.")
            else:
                break
        while True:
            try:
                continente = input("ingrese continente de destino: ")
                if continente.lower() in ("europa","asia","oceania","oceanía"):
                    break
                else:
                    print(f"Debe de ser un continente valido.")
            except ValueError as e:
                print(f"Por favor elige bien el continente, AWEONAO.")
        while True:
            try:
                litros = float(input("ingrese litros a exportar: "))
                if litros > 0:
                    break
                else:
                    print(f"El valor de los litros debe ser mayor a 0, tu pusiste {litros} litros")
            except ValueError:
                print(f"El valor debe ser un numero decimal o entero.")
            except Exception as e:
                print(f"Algo ocurrió!. Volviendo al menú principal...")
                break

        break
    except ValueError:
        print("no válido")
    except Exception as e:
        print("Error: ",e.with_traceback)

# Calculos
## Cantidad tanktainers
nTanktainers = litros // tanktainer_litros

if litros % tanktainer_litros != 0:
    nTanktainers += 1

## Valor tanktainers
valorTanktainers = nTanktainers * costo_tanktainer

## Cantidad botellas y valor total
cantidad_botellas = 0
valor_total_botellas = 0
### Cantidad y valor depende del continente
if continente == "asia":
    cantidad_botellas = round(litros / asia_litros,2)
    valor_total_botellas = cantidad_botellas * costo_asia
elif continente == "europa":
    cantidad_botellas = round(litros / europa_litros,2)
    valor_total_botellas = cantidad_botellas * costo_europa
elif continente in ("oceania","oceanía"):
    cantidad_botellas = round(litros / oceania_litros,2)
    valor_total_botellas = cantidad_botellas * costo_oceania

# Valor total exportacion
valor_total = valorTanktainers + valor_total_botellas



print(f"-- DATOS COTIZANTE --")
print(f"Nombre : {nombre}")
print(f"Fono contacto : {fono}")
print(f"Continente a exportar : {continente.capitalize()}")
print(f"Litros a exportar : {litros}")

print(f"-- Cotización  --")
print(f"Cantidad tanktainers : {nTanktainers}")
print(f"Costo tanktainers : {valorTanktainers}")
print(f"Cantidad botellas : {cantidad_botellas}")
print(f"Valor total botellas : USD${valor_total_botellas:,}")
print(f"Valor final cotización : USD${valor_total:n}")