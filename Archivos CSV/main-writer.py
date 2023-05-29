import csv

data = [
    ["Name", "Age", "Gender"],
    ["John", 25, "Male"],
    ["Mary", 23, "Female"],
    ["Peter", 27, "Male"],
]

with open("output-writer.csv", "w") as f:
    writer = csv.writer(f)
    writer.writerows(data)
