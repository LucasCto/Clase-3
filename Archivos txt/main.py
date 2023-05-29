# Path: archivo_ejemplo.txt
ruta = "archivo_ejemplo.txt"
archivo = open(ruta, "r")
contenido = archivo.read()
print(contenido)
archivo.close() # IMPORTANTE: Cerrar el archivo

# Utilizando with
with open(ruta, "r") as archivo:
    contenido = archivo.read()
    print(contenido)


# Escribir en un archivo
# Path: archivo_ejemplo.txt
ruta = "archivo_ejemplo.txt"
archivo = open(ruta, "w")
archivo.write("Hola mundo")
archivo.close()

# Utilizando with
with open(ruta, "w") as archivo:
    archivo.write("Hola mundo")

# Agregar contenido a un archivo
# Path: archivo_ejemplo.txt
ruta = "archivo_ejemplo.txt"
archivo = open(ruta, "a")
archivo.write("Hola mundo")
archivo.close()

# Utilizando with
with open(ruta, "a") as archivo:
    archivo.write("Hola mundo")


