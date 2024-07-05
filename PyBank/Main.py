#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os
import csv
import pandas as pd

Budget_csv = os.path.join('..', "Pybank", "Resources", "budget_data.csv")

profits_losses = []

with open(Budget_csv, mode='r', encoding='utf-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)
    df = pd.read_csv(Budget_csv) #Convert csv in dataframe
    Total_P = len(df) # Get number of lines in dataframe (number of months)
    for row in csvreader:
        profits_losses.append(int(row[1])) #Create a list of changes between months

Total_Amount = "${:.0f}".format(sum(profits_losses)) # Get the total of Profit-Losses in database
monthly_chg = [profits_losses[i] - profits_losses[i - 1] for i in range(1, len(profits_losses))] # Get the list of Profit-Losses changes in database
avg_chg = sum(monthly_chg) / len(monthly_chg) # Get the mean of Profit-Losses in database

max_change = max(monthly_chg) #Get max and min changes between periods in the database  
min_change = min(monthly_chg)

max_chg_idx = monthly_chg.index(max_change) + 1 #Get max and min changes index in the changes (P&L) list
min_chg_idx = monthly_chg.index(min_change) + 1

max_chg_period = df.loc[max_chg_idx, 'Date'] #Get period name of max/min changes
min_chg_period = df.loc[min_chg_idx, 'Date']

# Print resutls
print("Financial Analysis")    
print("--------------------------------------------")
print("Total months: ", Total_P)
print("Total: ", Total_Amount)
print("Average Change: ", "${:.2f}".format(avg_chg))
print(f'Greatest Increase in Profits: {max_chg_period} (${max_change})')
print(f'Greatest Decrease in Profits: {min_chg_period} (${min_change})')

#Write results to a txt file
with open("Financial Analysis.txt", "w") as file:
    file.write("Financial Analysis\n")
    file.write("....................................................................................\n")
    file.write("Total months: " + str(Total_P) + "\n")
    file.write("Total: " + Total_Amount + "\n")
    file.write("Average change: " + "${:.2f}".format(avg_chg) + "\n")
    file.write(f"Greatest Increase in Profits:   {max_chg_period}  (${max_change})\n" )
    file.write(f"Greatest Decrease in Profits:   {min_chg_period}  (${min_change})\n" )

