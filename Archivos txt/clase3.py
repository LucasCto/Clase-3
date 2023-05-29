ruta = "nuevo-archivo.txt"

# archivo = open(ruta, "w")
# archivo.write("Hola mundo")
# archivo.close()


# with open("nuevo-archivo.txt", "w") as archivo:
#     archivo.write("Hola mundo")


with open(ruta, "a") as archivo:
    archivo.write("Hola mundo")
