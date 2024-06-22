import lista_de_funciones as fn

####
lista_de_datos = fn.obtener_datos_csv('estudiantes.csv')

for i in range(1,len(lista_de_datos)):
    print(lista_de_datos[i][6])