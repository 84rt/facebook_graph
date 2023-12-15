import csv

your_name = "Bart Jaworski"

# Open the csv file and read it as a list of rows
with open(f"{your_name}.csv", "r") as f:
    reader = csv.reader(f)
    rows = list(reader)

out_a = []

with open(f"{your_name}.csv", "w") as f:
    for row in rows:
        f.write("[[" + row[1] + "]]\n")