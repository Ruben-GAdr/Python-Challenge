#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Import libraries
import os
import csv
# set resource
Election = os.path.join('..', "PyPoll", "Resources", "Election_data.csv")

num_rows  = 0 #Set variable to loop lines
id_candidate= [] #Set list for candidate names
candidate_n = [] #Set list for final candidate list
votes = [] #Set list for votes
pct_vote =[] #Set list for percentage votes

# In[2]:

# Load csv file 
with open(Election, mode='r', encoding='utf-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    data=list(csvreader) #Load data
    universe = len(data) #Count rows in data
    #print (universe)

    #Get list of candidate names
    for i in range (0,universe):
        candidate = data[i][2]
        id_candidate.append(candidate)
        if candidate not in candidate_n: 
            candidate_n.append(candidate)
    candidate_c = len(candidate_n)

    #Get count and percentage of votes
    for c in range (0,candidate_c):
        name = candidate_n[c]
        votes.append(id_candidate.count(name))
        votespct = votes[c]/universe
        pct_vote.append(votespct)
        winner = votes.index(max(votes))
# In[3]:
#Put result lines in a list
results = [] 
results.append("Election Results")
results.append("")
results.append("----------------------------")
results.append("")
results.append(f"Total Votes: {universe:}")
results.append("")
results.append("----------------------------")
results.append("")
for r in range(0,candidate_c):
    results.append(f"{candidate_n[r]}: {pct_vote[r]:.3%} ({votes[r]:})")
    results.append("")
results.append("----------------------------")
results.append("")
results.append(f"Winner: {candidate_n[winner]}")
results.append("")
results.append("----------------------------")
#Print lines in terminal
for line in results: #Print Results
    print(line)

#Write line results in analysis folder
output_file_path = os.path.join("..","PyPoll","Analysis",'election_results.txt') #Write Results in a txt file
with open(output_file_path, 'w') as file:
    for line in results:
        file.write(line + '\n')

