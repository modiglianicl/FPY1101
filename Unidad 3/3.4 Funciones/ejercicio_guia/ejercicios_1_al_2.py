## Funciones

# 1
def tamano_palabra(palabra):
    largo_palabra = 0
    for i in palabra:
        largo_palabra +=1
    return largo_palabra

# 2
def espar(numero):
    numero = float(numero)
    if numero % 2 == 0:
        return "Par!"
    else:
        return "Impar!"




# 1
largo_hola = tamano_palabra("hola123123")
print(largo_hola)

# 2
par_check = espar(2222222222)
print(par_check)

