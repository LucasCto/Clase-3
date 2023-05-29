#Contexto para usar el archivo csv: para poder encontrar si fuera un policia y quiero hacer una multa
#donde esta radicado el vehiculo y tambien quien es el dueño
#tambien sirve para buscar por patentes en caso de solo tener la patente del vehiculo
#y otra utilidad es la de añadir nuevas patentes en caso de que esta no hayan sido añadidas al sistema
#tambien si el dueño no es el correcto poder modificar dicho dato
#que me haga un archivo nuevo con todas la informacion, ingresando una provinicia
import numpy as np
import pandas as pd
import csv

def buscador_por_patente(data):
    patente = input("Ingrese la patente: ")
    vector = np.asarray(data[:,1])
    for datos in vector:
        if datos == patente:
            print("Patente encontrada")
            print(datos)
        else:
            print("Disculpe, no se encontró la patente")
            
def nuevo_ingreso():
    nombre = input("Ingres nombre y apellido (ej, Maria Paz): \n")
    patente = input("Ingrese patente: ")
    provincia = input("Ingrese la ubicación de donde esta radicado el automotor: \n")
    id = len(data)
    with open('patentes.csv') as nuevo:
        nuevo.write(f'0{id + 1},{patente},{nombre},{provincia}')

def eliminar_patente():
    patentes = np.asarray(data)
    buscador = input("Ingrese la patente a eliminar: ")
    resultado = np.where(patentes == buscador)
    if len(resultado[0]) > 0:
        indice_encontrado = resultado[0][0]
        print(f"El valor {buscador} fue encontrado en el índice {indice_encontrado}.")
        matriz_nueva = np.delete(patentes, indice_encontrado, axis=0)
        with open('patentes.csv', 'w', newline='') as archivo:
            escritor_csv = csv.writer(archivo)
            for fila in matriz_nueva:
                escritor_csv.writerow(fila)
    else:
        print(f"El valor {buscador} no fue encontrado en el arreglo.")

def nuevo_archivo_provincia():
    provincia = input("Ingrese la provincia: ")
    matriz = np.asarray(data)
    matriz_provincia = np.any(matriz[provincia])
    with open(f'{provincia}.csv', 'w') as f:
        f.write(matriz_provincia)


data = pd.read_csv('patentes.csv')
while True:
    print("-----Menu------")
    print(" a-Mostrar patentes "
          "\n b-Buscador "
          "\n c-Ingresar nuevo registro"
          "\n d-Generar nuevo archivo por provincia"
          "\n e-Eliminar un registro"
          "\n f-Salir")
    menu = input("Ingrese la opción a realizar: ")
    if menu == "a":
        print(data)
    elif menu == "b":
        buscador_por_patente(data)
    elif menu == "c":
        nuevo_ingreso()
    elif menu == "d:":
        nuevo_archivo_provincia()
    elif menu == "e":
        eliminar_patente()
    elif menu == "f":
        print("Hasta luego!")
        break
    else:
        print("Error, intente nuevamente")