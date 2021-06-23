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
# Lists and dictionaries to store data
data = []
unique_candidates = [] 
candidate_votes = []

candidates = {}
candidate_percentages = {}

with open(election_csv) as file:
    csvreader = csv.reader(file, delimiter=",")
    header = next(csvreader)
    for row in csvreader:

        #create data list
        data.append(row)

        #create list of candidate names from every row
        candidate_votes.append(row[2])

    #create candidate list and print to view complete list of unique candidates
    unique_candidates = set(candidate_votes)

    for candidate in unique_candidates:
        candidates[candidate] = 0

    #Calculate total votes
    total_votes = len(data)
    
    #calculate the number of votes for each candidate
    for vote in candidate_votes:
        candidates[vote] += 1

    #Calculate the vote percentage for each candidate
    for candidate in unique_candidates:
        vote_count = candidates[candidate]
        candidate_percentages[candidate] = '{0:.3f}'.format(vote_count/total_votes *100)

    #Identify the winner
    winner_name = ""
    winner_votes = 0
    winner_pct = 0
    for key, value in candidates.items():
        if value > winner_votes:
            winner_votes = value
            winner_name = key
            winner_percent = candidate_percentages[key]

#print results
print("Election Results")
print("------------------------")
print(f"Total Votes:  {total_votes}")
print("------------------------")
for w in sorted(candidates, key=candidates.get, reverse=True):
    print(f"{w}: {candidate_percentages[w]}% ({candidates[w]})")
print("------------------------")
print(f"Winner: {winner_name}")
print("------------------------")


# Set variable for output file
output_file = os.path.join("Analysis",  "PyPoll_Analysis.txt")

#  Open the output file
with open(output_file, "w") as text_file:

#Write to text file

    text_file.write("Election Results\n")
    text_file.write("------------------------\n")
    text_file.write(f"Total Votes:  {total_votes}\n")
    text_file.write("------------------------\n")
    for w in sorted(candidates, key=candidates.get, reverse=True):
        text_file.write(f"{w}: {candidate_percentages[w]}% ({candidates[w]})\n")
    text_file.write("------------------------\n")
    text_file.write(f"Winner: {winner_name}\n")
    text_file.write("------------------------\n")



