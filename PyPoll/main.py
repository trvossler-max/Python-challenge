# Calculate total number of votes
# Create a complete list of candidates who received votes
# Calculate the percentage of votes each candidate won
# Caculate the total number of votes each candidate won
# Determine the winner of the election based on popular vote
import os
import csv

#Path to collect data from the csv file
election_csv = os.path.join("Resources", "election_data.csv")

# Lists to store data
data = []
candidate = [] 
all_candidates = []
date = []
change = []

polldict = {}

with open(election_csv) as file:
    csvreader = csv.reader(file, delimiter=",")
    header = next(csvreader)
    for row in csvreader:

    #create data list
        data.append(row)

    #create list of candidate names from every row
        all_candidates.append(row[2])

    #create candidate list
        if row[2] not in candidate:
            candidate.append(row[2])

    #create dictionary
        polldict = {(row[0]):(row[2])}


    #declare 
        v=list(polldict.values())
        k=list(polldict.keys()) 
        m=max(polldict, key=polldict.get) 

    #print dictionary values
    
    print(m)

    #calculate total number of votes
    print(f"Total Votes:  {str(len(data))}")

    #create a complete list of candidates
    print(candidate)

    #Calculate total votes for each candidate
    print(all_candidates.count("Correy"))
    print(all_candidates.count("Khan"))
    print(all_candidates.count("Li"))
    print(all_candidates.count("O'Tooley"))

    print(f"Greatest Decrease in Profits:  {str(min_dt_chng)} (${str(min_value)})")

    #Calculate total votes for each candidate based on using the dictionary
    max_value=0
    winner = ""
    for i in polldict:
        votes=polldict[i]
        if int(votes) > max_value:
            max_value = votes
            winner = i
    print('-------------------------------------------')
    print(f'Winner:         {i}')
    print('-------------------------------------------')


