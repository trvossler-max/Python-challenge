import os
import csv

wrestling_csv = os.path.join('..', 'Resources', 'wwe-data-2016.csv')

with open (werstling_csv) as file:
    csvreader = csv.reader(file)
    header = next(csvreader)
    data = []
    for row in csvreader:
        data.append(row)

print(len(data))  

total = 0
for row in data:
    total += int(row[2])

print(total)   


