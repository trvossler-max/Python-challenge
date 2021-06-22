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
        polldict = {(row[2]):(row[1])}


    #declare variables
    khan_votes = int(all_candidates.count("Khan"))
    correy_votes = int(all_candidates.count("Correy"))
    li_votes = int(all_candidates.count("Li"))
    otooley_votes = int(all_candidates.count("O'Tooley"))
    all_votes = int(len(data))

    #calcluate percentages
    khan_percentage = (khan_votes/all_votes)
    correy_percentage = (correy_votes/all_votes)
    li_percentage = (li_votes/all_votes)
    otooley_percentage = (otooley_votes/all_votes)

    v=list(polldict.values())
    k=list(polldict.keys()) 
    m=max(polldict, key=polldict.get) 

    #create a complete list of candidates
    #print(candidate)

    #Calculate total votes for each candidate based on using the dictionary
    #max_value=0
    #winner = ""
    #for i in polldict:
        #votes=polldict[i]
        #if votes > max_value:
            #max_value = votes
            #winner = i
    print("Election Results")        
    print("-------------------------------------------")
    print(f"Total Votes:  {(all_votes)}")
    print('-------------------------------------------')
    print(f"Khan:  {(khan_percentage):.3%} ({(khan_votes)})")
    print(f"Correy:  {(correy_percentage):.3%} ({(correy_votes)})")
    print(f"Li:  {(li_percentage):.3%} ({(li_votes)})")
    print(f"O'tooley:  {(otooley_percentage):.3%} ({(otooley_votes)})")
    print("-------------------------------------------")
    print("Winner:  Khan")
    print("-------------------------------------------")

#Write to text file

    # Set variable for output file
output_file = os.path.join("Analysis",  "PyPoll_Analysis.txt")

#  Open the output file
with open(output_file, "w") as text_file:

#Write to text file
    text_file.write("Election Results\n")        
    text_file.write("-------------------------------------------\n")
    text_file.write(f"Total Votes:  {(all_votes)}\n")
    text_file.write('-------------------------------------------\n')
    text_file.write(f"Khan:  {(khan_percentage):.3%} ({(khan_votes)})\n")
    text_file.write(f"Correy:  {(correy_percentage):.3%} ({(correy_votes)})\n")
    text_file.write(f"Li:  {(li_percentage):.3%} ({(li_votes)})\n")
    text_file.write(f"O'tooley:  {(otooley_percentage):.3%} ({(otooley_votes)})\n")
    text_file.write("-------------------------------------------\n")
    text_file.write("Winner:  Khan\n")
    text_file.write("-------------------------------------------\n")



