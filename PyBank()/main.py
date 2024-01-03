# Importing Usual Dependencies, [Os,Csv]
import os 
import csv

# Create variables to hold in start data
TotalMonths = 0
Total = 0
PreviousProfitLoss = None
ProfitLossChanges = []
Dates = []

# Using <os.path.join( )> to set a path named 'file_path'
file_path = os.path.join( "Resources", "budget_data.csv")

# Used <open( )> to open the document from the path
# Used <csv.reader( )> to read the file with a delimiter of "," to separate by commas
# Used <next(csvreader)> to go to the next line in sequence
with open(file_path, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    header = next(csvreader)

    # Using ForLoop through each row in the CSV file
    for row in csvreader:
        # Extract data from the row, extracting 'date' and 'profit_loss' from first and second row [0,1].
        # Used < int( ) > to gather data in integer format from the second row 'row[1]' 
       
        date = row[0]
        profit_loss = int(row[1])

        # Calculating total months and net total
        # Using < += > to sum up and place into same variable
        TotalMonths += 1
        Total += profit_loss

        # Using if statement on 'PreviousProfitLoss' when it contains data to calculate 'change'
        # Using < .append( ) > to add the 'change' to the 'ProfitLossChanges'
        # Using < .append( ) > to add the 'date' to 'Dates'
        if PreviousProfitLoss is not None:
            change = profit_loss - PreviousProfitLoss
            ProfitLossChanges.append(change)
            Dates.append(date)

        # Update previous profit/loss for the next iteration
        PreviousProfitLoss = profit_loss

# Calculating average change in Profit/Loss
# Using <round( )> to round the final output
# Using < sum( )/ len( ) > to calculate the average
average_change = round(sum(ProfitLossChanges) / len(ProfitLossChanges), 2)

# Finding the greatest increase and greatest decrease in profit/loss
# Using < max( ) > to figure out highest data point
# Using < .index( ) > to look into [ProfitLossChanges] with 'greatest_increase' to find out the "Dates"
greatest_increase = max(ProfitLossChanges)
greatest_increase_date = Dates[ProfitLossChanges.index(greatest_increase)]
# Using < min( ) > to figure out lowest data point
greatest_decrease = min(ProfitLossChanges)
greatest_decrease_date = Dates[ProfitLossChanges.index(greatest_decrease)]

# Printing the financial analysis
print("Financial Analysis")
print("------------------")
print(f"Total Months: {TotalMonths}")
print(f"Total: ${Total}")
print(f"Average Change: ${average_change}")
print(f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})")
print(f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})")

# Saving the results to a text file 
output_file = "Financial_Analysis.txt"
with open(output_file, "w") as textfile:
    textfile.write("Financial Analysis\n")
    textfile.write("------------------\n")
    textfile.write(f"Total Months: {TotalMonths}\n")
    textfile.write(f"Total: ${Total}\n")
    textfile.write(f"Average Change: ${average_change}")
    textfile.write(f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})\n")
    textfile.write(f"Greatest Decrease in Losses: {greatest_decrease_date} (${greatest_decrease})\n")

print("Results saved to 'Financial_Analysis.txt'")

