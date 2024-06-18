import json
# Inicializo lista para agregar cada diccionario
json_dump = []

# Abro el archivo
with open('archivo.json','r',encoding='utf-8') as archivo:
    datos_raw = json.load(archivo)
    for i in datos_raw:
        json_dump.append(i)

# Inicializo lista con todas las asistencas
asistencias = []

# Dumpeo todas las asistencias a "asistencias"
for i in json_dump:
    if i['asistencia_final'] == 'asistencia_final':
        continue
    asistencias.append((int(i['asistencia_final'])))

# Resultados
print(f"Asistencias : {asistencias}")
prom_asistencias = round(sum(asistencias) / len(asistencias),2)
print(f"La asistencia promedio del curso es {prom_asistencias}")

