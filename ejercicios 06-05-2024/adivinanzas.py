import random

numero_pc = random.randint(1,100)
print(f"El numero es {numero_pc}")
guess = -1

while numero_pc != guess:
    guess = int(input("Adivina un numero entre 1 y 100 : "))
    if guess == numero_pc:
        print("Ganaste")
        break
    elif (guess-numero_pc) <= 50:
        print(f"Demasiado bajo")
        continue
    elif (guess-numero_pc) > 50:
        print(f"Demasiado alto")
        continue
