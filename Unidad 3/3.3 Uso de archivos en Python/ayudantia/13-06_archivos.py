import csv

#w = escritura
#r = lectura
#r+ = lectura y escritura

with open('nuevo_archivo.csv','w',newline='') as csvfile:
    writer = csv.writer(csvfile,lineterminator='\n')
    writer.writerow(['nombre','apellido','edad'])
    writer.writerows([
        ['felipe','villarroel','32'],
        ['cesar','toro','28']
        ])
    


with open('nuevo_archivo.csv','r',newline='') as csvfile:
    lector = csv.reader(csvfile)
    for fila in lector:
        print(fila)