#allow creation of file paths across operating systems
import os

#Import module to read CSV files
import csv

#define path to csv file
csvpath = os.path.join(".", "Resources", "budget_data.csv")

#Name lists to store data
date = []
profit_loss = []
change = []
open_value = 0
close_value = 0
avg_change = 0
greatest_incr_date = 0
greatest_incr_profit = 0
greatest_decr_date = 0
greatest_decr_profit = 0

#open and read csv file
with open(csvpath) as csvfile:
        csvreader = csv.reader(csvfile, delimiter=",")

        # Read the header row first
        csvheader = next(csvfile)

        for row in csvreader:
                #add date
                date.append(row[0])

                #add profit_loss as an integer
                profit_loss.append(int(row[1]))
               
                        
#calculate the total number of months in the dataset
total_months = len(date)   


#calculate net total amount of Profit/Losses
profit_loss_net = sum(profit_loss)

#calculate changes in Profit/Losses
for x in range(1, total_months):
      delta = profit_loss[x] - profit_loss[x-1]
      change.append(delta)

#average the change in profit and loss
avg_change = sum(change) / len(change)

#Deterime the greatest increase and decrease in profit
greatest_incr = max(change)
greatest_incr_date = date[change.index(greatest_incr) + 1]
greatest_decr = min(change)
greatest_decr_date = date[change.index(greatest_decr) + 1]

#Print analysis to terminal
print(f"Financial Analysis")
print(f"-----------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${profit_loss_net}")
print(f"Average Change: ${avg_change:.2f}")
print(f"Greatest Increase in Profits: {greatest_incr_date} (${greatest_incr})")
print(f"Greatest Decrease in Profits: {greatest_decr_date} (${greatest_decr})")

# export to text file
f = open("analysis/results.txt","w")

print(f"Financial Analysis", file=f)
print(f"-----------------------------", file=f)
print(f"Total Months: {total_months}", file=f)
print(f"Total: ${profit_loss_net}", file=f)
print(f"Average Change: ${avg_change:.2f}", file=f)
print(f"Greatest Increase in Profits: {greatest_incr_date} (${greatest_incr})", file=f)
print(f"Greatest Decrease in Profits: {greatest_decr_date} (${greatest_decr})", file=f)

f.close()



 
