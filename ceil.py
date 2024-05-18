# Sumando + 1 si sobra de la división
total = 13000
divisor = 12000
cantidad = total//divisor
sobrante = total%divisor

if cantidad != 0 and sobrante > 0:
    print(f"Sobran : {sobrante}")
    cantidad +=1
else:
    print(f"No sobra {sobrante}")

print(cantidad)