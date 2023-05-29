import csv
import numpy as np
print("Hola")


#with open("cities.csv", 'r') as f:
#    data = csv.reader(f)
#    for fila in data:
#        print(fila)
#        if str(fila).startswith('S'):
#            print(fila)


data = np.genfromtxt('cities.csv', delimiter=',')

ciudades = data[:,8]
letra_inicio = ' "S"'
buscar_ciudades = ciudades[np.char.startswith(ciudades, letra_inicio)]
print(buscar_ciudades)
for datos in ciudades:
    print(datos)

