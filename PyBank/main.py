#allow creation of file paths across operating systems
import os

#Import module to read CSV files
import csv

#define path to csv file
csvpath = os.path.join(".", "Resources", "budget_data.csv")

#Name lists to store data
date = []
profit_loss = []
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
        #Skip header row
        next(csvreader, None)

#def print_changes(change_data):
        #date = str(change_data[0])
        #profit_loss = int(change_data[1])

        for row in csvreader:
                #add date
                date.append(row[0])
                open_value = date(row[0])

                #add profit_loss
                profit_loss.append(row[1])
                if profit_loss >= greatest_incr_profit:
                        greatest_incr_profit.append(profit_loss)
                elif profit_loss <= greatest_decr_profit:
                        greatest_decr_profit.append(profit_loss)
                else:
                        pass
                        
#calculate the total number of months in the dataset
total_months = len(date)  
print(total_months)  
print(open_value)

profit_loss = [int(i) for i in profit_loss]
    for x in range(profit_loss):
    print(sum(profit_loss))
    profit_loss_net = sum(profit_loss)

#Sum of profit and loss over period
profit_loss_net = sum(profit_loss)

#calculate the change in profit and loss and then average
avg_change = [close_value - open_value] / [total_months - 1]

#Deterime the greatest increase and decrease in profit

#Print analysis
print("Financial Analysis")
print("-----------------------------")
print(f"Total Months: {total_months")
print(f"Total: ${profit_loss_net}")
print(f"Average Change: {}")
print(f"Greatest Increase in Profits: {greatest_incr_date} {greatest_incr_profit}")
print(f"Greatest Decrease in Profits: {greatest_decr_date} {greatest_decr_profit}")

#export text file
def write_to_file(filename, lines):
     with open(filename,"w") as text:
        for line in lines:
            text.write(f"{line}\n")


 
