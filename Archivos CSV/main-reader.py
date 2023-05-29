import csv

with open("dummy-data.csv", "r") as f:
    reader = csv.reader(f)
    suma = 0
    for row in reader:
        suma += int(row[1])

    print("promedio de edades:", suma / 4)
