#allow creation of file paths across operating systems
import os

#Import module to read CSV files
import csv

#define path to csv file
csvpath = os.path.join(".", "Resources", "election_data.csv")

#total votes
total_ballots = 0
#list of candidates
candidates = []
#percentage of votes each candidate
percent_votes = []
#total number of votes each candidate
number_votes = {}
#winner of election


#open and read csv file
with open(csvpath) as csvfile:
        csvreader = csv.reader(csvfile, delimiter=",")

        #Skip header row
        csvheader = next(csvfile)

        for row in csvreader:
                #add to total votes
                total_ballots += 1

                #add candidate to list and count candidate votes
                candidate_name = row[2]
                if candidate_name in number_votes:
                       number_votes[candidate_name] +=1
                else:
                       number_votes[candidate_name] = 1
             

#percentage of votes for each candidate
results = []
for candidate, votes in number_votes.items():
      percentage = (votes / total_ballots) * 100
      results.append((candidate, percentage, votes))  

#determine winner based on popular vote
winner = max(results, key=lambda x: x[2])


#Print to terminal
print("Election Results")
print("------------------------")
print(f"Total Votes: {total_ballots}")
print("------------------------")
for candidate, percentage, votes in results:
    print(f"{candidate}: {percentage:.3f}% ({votes})")
print("------------------------")
print(f"Winner: {winner[0]}")
print("------------------------")

# export to text file
f = open("analysis/results.txt","w")

print("Election Results", file=f)
print("------------------------", file=f)
print(f"Total Votes: {total_ballots}", file=f)
print("------------------------", file=f)
for candidate, percentage, votes in results:
    print(f"{candidate}: {percentage:.3f}% ({votes})", file=f)
print("------------------------", file=f)
print(f"Winner: {winner[0]}", file=f)
print("------------------------", file=f)

f.close()


 
