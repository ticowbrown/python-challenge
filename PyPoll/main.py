# First we'll import the os module
# This will allow us to create file paths across operating systems
import os

# Module for reading CSV files
import csv

# Path to the CSV file
csvpath = os.path.join('Resources','election_data.csv')


# Initialize variables to store analysis results
total_votes = 0
candidates = {}
winner = ""
max_votes = 0

# Read the CSV file
with open(csvpath, newline="") as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=",")

    # Skip the header
    next(csvreader)

    # Loop through rows in the CSV file
    for row in csvreader:
        # Extract candidate name
        candidate_name = row[2]

        # Count total votes
        total_votes += 1

        # Add candidate to the dictionary if not already present
        if candidate_name not in candidates:
            candidates[candidate_name] = 0

        # Increment candidate's vote count
        candidates[candidate_name] += 1
 

     # Check for the winner
for candidate, votes, in candidates.items():       
    if votes > max_votes:
        max_votes = votes
        winner = candidate

# Print the analysis results
        
print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")

# Calculate the percentage of votes and find the winner
for candidate, votes in candidates.items():
    percentage = (votes / total_votes) * 100
    print(f"{candidate}: {percentage:.3f}% ({votes})")


print("-------------------------")
print(f"Winner: {winner}")
print("-------------------------")

# Prepare to write the analysis results
analysis_results = []
analysis_results.append("Election Results")
analysis_results.append("-------------------------")
analysis_results.append(f"Total Votes: {total_votes}")
analysis_results.append("-------------------------")

# Calculate candidates' votes and percentages
for candidate, votes in candidates.items():
    percentage = (votes / total_votes) * 100
    analysis_results.append(f"{candidate}: {percentage:.3f}% ({votes})")

analysis_results.append("-------------------------")
analysis_results.append(f"Winner: {winner}")
analysis_results.append("-------------------------")

#Set vriable for output path
output_path = os.path.join('Analysis','PyPoll_Analysis.txt')

# Write the analysis results to a file
with open(output_path, "w", newline='') as f:
    writer = csv.writer(f)
      
    for line in analysis_results:
       f.write(line + "\n")