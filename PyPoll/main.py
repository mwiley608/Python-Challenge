#allow creation of file paths across operating systems
import os

#Import module to read CSV files
import csv

#define path to csv file
csvpath = os.path.join(".", "Resources", "election_data.csv")

#Name lists to store data
ballot = []
county = []
candidate= []

#open and read csv file
with open(csvpath) as csvfile:
        csvreader = csv.reader(csvfile, delimiter=",")
        #Skip header row
        next(csvreader, None)

        for row in csvreader:
                #list ballots
                ballot.append(row[0])
               
                #list counties
                county.append(row[1])
                
                #list candidates
                candidate.append(row[2])
             
#calculate the total number of votes
total_ballots = len(ballot)
print(total_ballots)

#list of candidates

#total number of votes for each candidate

#percentage of votes for each candidate

#determine winner

#Print analysis
print("Election Results")
print("------------------------")
print(f"Total Votes: {total_ballots}")
print("------------------------")
print(f"Winner: ")
print("------------------------")

#export text file
def write_to_file(filename, lines):
     with open(filename,"w") as text:
        for line in lines:
            text.write(f"{line}\n")


 
