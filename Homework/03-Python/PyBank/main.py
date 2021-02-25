import os
import csv

# Path to collect data from the Resources folder
py_bank_csv = os.path.join('.', 'Resources', 'PyBank_Resources_budget_data.csv')

def get_bank_data():
    # Open the CSV
    # Read through csv file
    with open(py_bank_csv, 'r') as pyBankCSVFile:
        totalProfit = 0
        average = 0
        changes = 0 
        dateArray = []
        profitsLossesArray = []
        changesInRevenue = []
        changesInRevenueDate = []

        # Split the data on commas
        csvreader = csv.reader(pyBankCSVFile, delimiter=',')
        header = next(csvreader)

        # Loop through the data and return average, increase and decrease in profits
        for row in csvreader:
            dateArray.append(row[0])
            profitsLossesArray.append(row[1])
            
            totalMonths = len(dateArray)
            totalProfit += int(row[1])
            
        for i in range(1, len(profitsLossesArray)):
            changesInRevenue.append(int(profitsLossesArray[i]) - int(profitsLossesArray[i - 1]))
            changesInRevenueDate.append(dateArray)
            profitInMonths =  str(dateArray[changesInRevenue.index(max(changesInRevenue)) + 1])
            decreaseInProfits = str(dateArray[changesInRevenue.index(min(changesInRevenue)) + 1])

        average = round(sum(changesInRevenue) / len(changesInRevenue), 2)
        increaseInProfits = max(changesInRevenue)
        decreaseInProfits = min(changesInRevenue)

    # Print to Terminal     
    print("Financial Analysis")       
    print("----------------------------")
    print(f"Total Months: {totalMonths}")
    print(f"Total Profit: {totalProfit}")
    print(f"Average: {average}")
    print(f"Greatest Increase in Profits: {profitInMonths} ({increaseInProfits})")
    print(f"Greatest Decrease in Profits: {profitInMonths} ({decreaseInProfits})")

    # Write to text file  
    file1 = open("./analysis/results.txt","w")
    file1.write("Financial Analysis\n")
    file1.write("----------------------------\n")
    file1.write(f"Total Months: {totalMonths}\n")
    file1.write(f"Total Profit: {totalProfit}\n")
    file1.write(f"Average: {average}\n")
    file1.write(f"Greatest Increase in Profits: {profitInMonths} ({increaseInProfits})\n")
    file1.write(f"Greatest Decrease in Profits: {profitInMonths} ({decreaseInProfits})\n")

get_bank_data()