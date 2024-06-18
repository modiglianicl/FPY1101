import json

json_dump = []

with open('archivo.json','r',encoding='utf-8') as archivo:
    datos_raw = json.load(archivo)
    for i in datos_raw:
        json_dump.append(i)


asistencias = []

for i in json_dump:
    if i['asistencia_final'] == 'asistencia_final':
        continue
    asistencias.append((int(i['asistencia_final'])))

print(f"Asistencias : {asistencias}")
prom_asistencias = round(sum(asistencias) / len(asistencias),2)
print(f"La asistencia promedio del curso es {prom_asistencias}")

