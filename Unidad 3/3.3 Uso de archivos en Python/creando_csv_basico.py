import csv
import json

with open("ejemplo.csv","w",newline="") as C:
    escritura = csv.writer(C)

    escritura.writerows({"nombre"})