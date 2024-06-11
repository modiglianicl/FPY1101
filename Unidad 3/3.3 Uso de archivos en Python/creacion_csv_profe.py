import csv 
import json

with open('ejercicio.csv', "w", newline='') as x:
    escritura = csv.writer(x)
    escritura.writerow(['Nombre','edad','Ciudad'])
    escritura.writerows([
['Esteban', 25, 'Santiago'],
['María', 30, 'Valparaíso'],
['Carlos', 22, 'Osorno'],
['Sigrid', 25, 'Santiago'],
['Daniela', 30, 'La Cisterna'],
['Aylen', 22, 'La florida']
])