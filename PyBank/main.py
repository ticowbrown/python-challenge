# First we'll import the os module
# This will allow us to create file paths across operating systems
import os

# Module for reading CSV files
import csv

# Path to the CSV file
csvpath = os.path.join('Resources','budget_data.csv')

# Initialize variables to store analysis results
total_months = 0
total_profit_loss = 0
previous_profit_loss = 0
profit_loss_changes = []
months = []


# Read the CSV file
with open(csvpath, newline="") as csvfile:
    
    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=",")
    
    # Read the header row first (skip this step if there is no header)
    csv_header = next(csvreader)

    # Loop through rows in the CSV file
    for row in csvreader:
        # Extract data
        date = row[0]
        profit_loss = int(row[1])

        # Calculate total months and total profit/loss
        total_months += 1
        total_profit_loss += profit_loss

        # Track profit/loss changes
        if previous_profit_loss != 0:
            change = profit_loss - previous_profit_loss
            profit_loss_changes.append(change)
            months.append(date)

        previous_profit_loss = profit_loss

# Calculate the average change in profit/loss
average_change = sum(profit_loss_changes) / len(profit_loss_changes)

# Find the greatest increase and decrease in profits
greatest_increase = max(profit_loss_changes)
greatest_decrease = min(profit_loss_changes)

# Find the corresponding months for the greatest increase and decrease
increase_month = months[profit_loss_changes.index(greatest_increase)]
decrease_month = months[profit_loss_changes.index(greatest_decrease)]

# Print the analysis results
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${total_profit_loss}")
print(f"Average Change: ${round(average_change, 2)}")
print(f"Greatest Increase in Profits: {increase_month} (${greatest_increase})")
print(f"Greatest Decrease in Profits: {decrease_month} (${greatest_decrease})")

# Prepare to write the analysis results
analysis_results = []
analysis_results.append("Financial Analysis")
analysis_results.append("-------------------------")
analysis_results.append(f"Total Months: {total_months}")
analysis_results.append(f"Total: ${total_profit_loss}")
analysis_results.append(f"Average Change: ${round(average_change, 2)}")
analysis_results.append(f"Greatest Increase in Profits: {increase_month} (${greatest_increase})")
analysis_results.append(f"Greatest Decrease in Profits: {decrease_month} (${greatest_decrease})")

#Set vriable for output path
output_path = os.path.join('Analysis','PyBank_Analysis.txt')

# Write the analysis results to a file
with open(output_path, "w", newline='') as f:
    writer = csv.writer(f)
      
    for line in analysis_results:
       f.write(line + "\n")