import lista_de_funciones as fn

lista_de_datos = fn.obtener_datos_csv('estudiantes.csv')
print("Promedio mas alto : ",fn.obtener_el_promedio_mas_alto(lista_de_datos))