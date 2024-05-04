# 1. Mensaje de inicio
print(f"¡Comienza la carrera!")

# 2. Primer Obstaculo - Valla
existe_valla = ""

## Asegurando que la respuesta sea solo si o no independiente las mayusculas
while (existe_valla.lower() != "si") or (existe_valla.lower() != "no"):
    existe_valla = input("Encontraste una valla? (si/no) \n")
    if existe_valla.lower() == "si":
        print("Salta la valla!")
        break
    elif existe_valla.lower() == "no":
        print("Sigue corriendo!")
        break

# 3 . Segundo obstaculo - Puente
existe_puente = ""

while (existe_puente.lower() != "si") or (existe_puente.lower() != "no"):
    existe_puente = input("Encontraste un puente? (si/no) \n")
    if existe_puente.lower() == "si":
        print("Atraviesa el túnel!")
        break
    elif existe_puente.lower() == "no":
        print("Sigue corriendo!")
        break

# 4. Tercer obstaculo - Laguna
existe_laguna = ""

while (existe_laguna.lower() != "si") or (existe_laguna.lower() != "no"):
    existe_laguna = input("Encontraste una laguna? (si/no) \n")
    if existe_laguna.lower() == "si":
        print("Debes nadar, pero te agotas!, has perdido!!")
        break
    elif existe_laguna.lower() == "no":
        print("Felicidades has llegado a la meta con éxito!")
        break

# 5. Fin del programa
    
print("El programa ha terminado")