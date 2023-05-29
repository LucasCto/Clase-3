import json

with open("data.json") as f:
    data = json.load(f)

    direccion = data["direccion"]
    calle = direccion["calle"]
    print("Direccion: ", direccion)
    print("Calle: ", calle)
