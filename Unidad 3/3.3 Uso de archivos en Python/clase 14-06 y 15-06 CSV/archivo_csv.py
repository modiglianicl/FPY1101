import csv

with open('datos.csv','w',newline='') as archivo:
    escribir_csv = csv.writer(archivo)

    escribir_csv.writerow(['nombre','apellido','nota_1','nota_2','nota_3','asistencia'])
    escribir_csv.writerows([
        ['felipe','villarroel',3,3,3,0.5],
        ['cesar','el toro',5,5,5,0.75],
        ['javier','asdsad',2,2,2,0.5]
                           ])
