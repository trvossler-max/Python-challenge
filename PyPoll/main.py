# Calculate total number of votes
# Create a complete list of candidates who received votes
# Calculate the percentage of votes each candidate won
# Caculate the total number of votes each candidate won
# Determine the winner of the election based on popular vote
import os
import csv

#Path to collect data from the csv file
election_csv = os.path.join("Resources", "election_data.csv")

# Lists and dictionaries to store data
data = []
candidates = [] 
all_candidates = []

polldict = {}
polldict_percentages = {}

with open(election_csv) as file:
    csvreader = csv.reader(file, delimiter=",")
    header = next(csvreader)
    for row in csvreader:

        #create data list
        data.append(row)

        #create list of candidate names from every row
        all_candidates.append(row[2])

        #create candidate list and print to view complete list of unique candidates
        if row[2] not in candidates:
            candidates.append(row[2])       

    for candidate in candidates:
        polldict[candidate] = int(all_candidates.count(candidate))
        polldict_percentages[candidate] = polldict[candidate] / len(all_candidates)

    #declare variables
    # khan_votes = int(all_candidates.count("Khan"))
    # correy_votes = int(all_candidates.count("Correy"))
    # li_votes = int(all_candidates.count("Li"))
    # otooley_votes = int(all_candidates.count("O'Tooley"))
    # all_votes = int(len(data))

election_results =f"""Election Results
-------------------------
Total Votes: {len(all_candidates)}
-------------------------
Khan: {polldict_percentages["Khan"]:.3%}% ({polldict["Khan"]})
Correy: {polldict_percentages["Correy"]:.3%}% ({polldict["Correy"]})
Li: {polldict_percentages["Li"]:.3%}% ({polldict["Li"]})
O'Tooley: {polldict_percentages["O'Tooley"]:.3%}% ({polldict["O'Tooley"]})
-------------------------
Winner: Khan
-------------------------"""

#Print to terminal
print(election_results)

# print(type(election_results))
# print(type(polldict_percentages))

# Set variable for output file
output_file = os.path.join("Analysis",  "PyPoll_Analysis.txt")

#  Open the output file
with open(output_file, "w") as text_file:

#Write to text file
    text_file.write(election_results)        




