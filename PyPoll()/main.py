# Imported Usual Dependencies [Os,Csv]
import os
import csv

# Created variables to store data into
TotalVotes = 0
Candidates = []
CandidateVotes = {}

# Reading the CSV file
# Used < os.path.join > to create a PATH to "election_data.csv"
file_path = os.path.join("Resources", "election_data.csv")

# With < open( ) > we opened the CSV file using the PATH.
# Using < csv.reader( ) > we can gather data and separate by the delimiter ","
# Using < next( ) > to go to the next line
with open(file_path, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    header = next(csvreader)

    # Looping through each row in the CSV file and adding +1 to the TotalVotes
    for row in csvreader:
        TotalVotes += 1
        candidate = row[2]

        # Update candidate list and count votes
        # If a new candidate appears add it to the 'Candidates' [] by using < .append > and set it to one
        # If no new candidate appears then just add a +1 to the respective column
        if candidate not in Candidates:
            Candidates.append(candidate)
            CandidateVotes[candidate] = 1
        else:
            CandidateVotes[candidate] += 1

# Determining the winner based on popular vote
# Used < max( ) > to find out the highest value in 'CandidateVotes'
winner = max(CandidateVotes, key=CandidateVotes.get)

# Print the analysis results
# Printing the Title "Election Results"
# Printing the Total Votes as well
# Used for loop to print each candidate from the [candidates] list and figuring out the percentage of votes from each candidate
print("Election Results")
print("-------------------------")
print(f"Total Votes: {TotalVotes}")
print("-------------------------")

for candidate in Candidates:
    votes = CandidateVotes[candidate]
    percentage = (votes / TotalVotes) * 100
    print(f"{candidate}: {percentage:.3f}% ({votes})")

print("-------------------------")
print(f"Winner: {winner}")
print("-------------------------")

# Saving the analysis results to a text file
# Using < open( ) > to open up the file and < textfile.write( ) > to write the data from [TotalVotes,Candidates,and Winner]
output_file = "Election_Results.txt"

with open(output_file, "w") as textfile:
    textfile.write("Election Results\n")
    textfile.write("-------------------------\n")
    textfile.write(f"Total Votes: {TotalVotes}\n")
    textfile.write("-------------------------\n")

    for candidate in Candidates:
        votes = CandidateVotes[candidate]
        percentage = (votes / TotalVotes) * 100
        textfile.write(f"{candidate}: {percentage:.3f}% ({votes})\n")

    textfile.write("-------------------------\n")
    textfile.write(f"Winner: {winner}\n")
    textfile.write("-------------------------\n")

print("Results saved to 'Election_Results.txt'")
