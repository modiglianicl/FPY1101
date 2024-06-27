# Librerias y funciones
import json
import os
import funciones_app_ej5 as fn

# Obtención de datos del usuario
usuario_nuevo = fn.registrar_usuario()

# Ruta del archivo
ruta_archivo = f"{os.getcwd()}/dato_usuario.json"

# Escritura del archivo
with open(ruta_archivo,"w",encoding='utf-8') as jsonfile:
    json.dump(usuario_nuevo,jsonfile,ensure_ascii=False,indent=4)