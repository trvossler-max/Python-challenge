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

# Lists to store data
data = []
total = []
date = []
change = []

with open(budget_csv) as file:
    csvreader = csv.reader(file, delimiter=",")
    header = next(csvreader)
    for row in csvreader:
        #create data list
        data.append(row)

        #create date list
        date.append(row[0])

        # Add total profit and losses
        total.append(int(row[1]))
    
print("Financial Analysis")
print("------------------------------------")

for i in range(1, len(total)):
    change.append(total[i] - total[i-1])
   

# Calculate the total number of months by counting the rows in the csv file  
print(f"Total Months:  {str(len(data))}")

 # Calculate the net total amount of profit/losses over the entire period
net_total = 0

for row in data:
    net_total += int(row[1])

print(f"Total:  ${str(net_total)}")

# Calculate the average of changes in profit/losses

avg_chng = round(sum(change) / len(change),2)

print(f"Average Change:  ${str(avg_chng)}")

# Caclulate the greatest increase in profits (date and amount) over the entire period
max_value = max(change)
max_dt_chng = date[change.index(max_value)+1]

print(f"Greatest Increase in Profits:  {str(max_dt_chng)} (${str(max_value)})")
    
# Calculate the greatest decrease in losses (date and amount) over the entire period 
min_value = min(change)
min_dt_chng = date[change.index(min_value)+1]

print(f"Greatest Decrease in Profits:  {str(min_dt_chng)} (${str(min_value)})")
    
# Set variable for output file
output_file = os.path.join("Analysis",  "PyBank_Analysis.txt")

#  Open the output file
with open(output_file, "w") as text_file:
    
    # Write to text file
    text_file.write("Financial Analysis\n")
    text_file.write("------------------------------------\n")
    text_file.write(f"Total Months:  {str(len(data))}\n")
    text_file.write(f"Total:  ${str(net_total)}\n")
    text_file.write(f"Average Change:  ${str(avg_chng)}\n")
    text_file.write(f"Greatest Increase in Profits:  {str(max_dt_chng)} (${str(max_value)})\n")
    text_file.write(f"Greatest Decrease in Profits:  {str(min_dt_chng)} (${str(min_value)})\n")


