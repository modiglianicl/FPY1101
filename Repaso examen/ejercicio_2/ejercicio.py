import funciones as fn
usuarios = fn.leer_archivo('usuarios.csv')
interacciones = fn.leer_archivo('interacciones.csv')

# Cantidad de likes
n_likes = fn.contar_likes(interacciones)
print(n_likes)

# Cantidad de comentarios
n_comentarios = fn.contar_comentarios(interacciones)
print(n_comentarios)

# Cantidad de interacciones

n_interacciones = fn.total_interacciones(interacciones)
print(n_interacciones)

# Calcular edad usuario (que cumple este año)
edad = fn.calcular_edad(usuarios[1][2])
print(edad)

# n usuarios con mas interacciones

datos_full = fn.unir_datos(usuarios,interacciones,3)

# Generamos el reporte en csv

fn.generar_csv(datos_full)
