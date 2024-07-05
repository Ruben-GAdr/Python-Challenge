#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Import libraries
import os
import csv
import pandas as pd
# set resource
Election = os.path.join('..', "PyPoll", "Resources", "Election_data.csv")


# In[2]:


# Load csv file 
with open(Election, mode='r', encoding='utf-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)
    df = pd.read_csv(Election) #Convert csv in dataframe
    Universe = len(df) # Get number of lines in dataframe (number of months)


# In[3]:


Candidates = df['Candidate'].unique() #Get candidates names
CandidatesV = df['Candidate'].value_counts() #Get candidates total votes
PctVotes = (CandidatesV/Universe)*100 #Get percent of votes 
Winner = CandidatesV.idxmax() #Get winner's name
print(PctVotes)


# In[4]:


results = [] #Put results in a list
  # Print the results to terminal
results.append("Election Results")
results.append("----------------------------")
results.append(f"Total Votes: {Universe:}")
results.append("----------------------------")
for Candidates in CandidatesV.index:
    votes = CandidatesV[Candidates]
    percentage = PctVotes[Candidates]
    results.append(f"{Candidates}: {percentage:.3f}% ({votes})")
results.append("----------------------------")
results.append(f"Winner: {Winner}")
results.append("----------------------------")
for line in results: #Print Results
    print(line)

output_file_path = 'election_results.txt' #Write Results in a txt file
with open(output_file_path, 'w') as file:
    for line in results:
        file.write(line + '\n')

