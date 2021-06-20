# Calculate the total number of months included in dataset
# Calculate the net total amount of profit/losses over the entire period
# Calculate the average of changes in profit/losses 
# Calculate the greatest increase in profits (date and amount) over the entire period.
# Calculate the greatest decrease in losses (date and amount over the entire period
# 
import os
import csv

#Path to collect data from the csv file
budget_csv = os.path.join("Resources", "budget_data.csv")

with open(budget_csv) as file:
    csvreader = csv.reader(file, delimiter=",")
    header = next(csvreader)

# Calculate the total number of months by counting the rows in the csv file
    data = []
    for row in csvreader:
        data.append(row)

    print(len(data))


    # Calculate the net total amount of profit/losses over the entire period
    net_total = 0

    for row in data:
        net_total += int(row[1])

    print(net_total)  

    numbers = (int(row[1]) for row in csvreader)
    total = sum(numbers)

    print(total)

    # Calculate the average of changes in profit/losses
    pandl = []
    for row in csvreader:
        pandl.append(row[1])
    
    change=[]
    for i in range(1, len(pandl)):
        change.append(pandl[i] - pandl[i-1])
        avg_chng = round(sum(change) / len(change),2)

        print(change)

    # Caclulate the greatest increase in profits (date and amount) over the entire period
        max_value = max(change)

        print(max_value)

    # Calculate the greatest decrease in losses (date and amount) over the entire period
      
        min_value = min(change)

        print(min_value)
 