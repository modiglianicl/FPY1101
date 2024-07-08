# Ejercicio 2
Ejercicio en el cual se practican funciones, analisis de datos en lista de listas, encontrar n maximos y por ultimo escribir un csv que proviene de una lista de listas.

# Funciones

## leer_archivo(<em>archivo.csv</em>)
Funcion que lee un archivo csv y retorna las filas como lista de listas , el primer elemento son los valores de las columnas
Retorna una matriz

## contar_likes(<em>datos</em>)
Funcion que recibe una lista de listas en donde busca si se encuentra la palabra "like" y va contando.
Retorna un int

## contar_comentarios(<em>datos</em>)
Funcion que recibe una lista de listas en donde busca si se encuentra la palabra "comment" y va contando.
Retorna un int

## total_interascciones(<em>datos</em>)
Funcion que ejecuta las dos funciones anteriores y las suma, dando como resultado el total de interacciones.
Retorna un int

## calcular_edad(<em>fecha</em>)
Funcion que calcula el año que <strong>debe cumplir</strong> la persona ese año.
devuelve un int

## unir_datos(<em>usuarios,interacciones,top=3</em>)
Funcion que realiza el analisis de cuantos likes,comentarios , total de transacciones, calcula la edad de la persona y categoriza a n cantidad de personas si esta dentro del top n.
Retorna una lista de listas.

## generar_csv(<em>datos</em>)
Escribe un csv con la matriz que se le entregue.
