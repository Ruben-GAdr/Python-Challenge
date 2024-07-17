#!/usr/bin/env python
# coding: utf-8

# Import libraries
import os
import csv

# Set path of CSV file
Budget_csv = os.path.join('..', "Pybank", "Resources", "budget_data.csv")

# Declare variables
total_p = 0
total_profit = 0
prev_profit = None
changes = []
g_increase = {"date": "", "amount": 0}
g_decrease = {"date": "", "amount": 0}

# Open csv file
with open(Budget_csv, mode='r', encoding='utf-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    data=list(csvreader) #Load data 
    total_p = len(data) #Count rows in data
    # loop through the dataset rows
    for row in data:
        date = row[0]
        profit = int(row[1])
        total_profit += profit # Sumamos total profit/losses
        if prev_profit is not None: #Calculate and append changes between periods
            change = profit - prev_profit
            changes.append(change)
            # Calculate max increase/decrease
            if change > g_increase["amount"]:
                g_increase = {"date": date, "amount": change}
            if change < g_decrease["amount"]:
                g_decrease = {"date": date, "amount": change}
        
        prev_profit = profit # set previous profit

avg_chg = round(sum(changes) / len(changes),2) if changes else 0 # Calculate average of changes

#Put result lines in a list
results = [] 
results.append("Financial Analysis") 
results.append("") 
results.append("--------------------------------------------")
results.append("") 
results.append(f"Total Months: {total_p}")
results.append("") 
results.append(f"Total: ${total_profit}")
results.append("") 
results.append(f"Average Change:  ${avg_chg}")
results.append("") 
results.append(f"Greatest Increase in Profits: {g_increase['date']} (${g_increase['amount']})")
results.append("") 
results.append(f"Greatest Decrease in Profits: {g_decrease['date']} (${g_decrease['amount']})")

#Print lines in terminal
for line in results: #Print Results
    print(line)

#Write results to a txt file
output_file_path = os.path.join("..","Pybank","Analysis",'Financial Analysis.txt') 
with open(output_file_path, "w") as file:
    for line in results:
        file.write(line + '\n')