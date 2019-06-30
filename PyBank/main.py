# Homework completed by Mohammad Zahid Shiwani, Adrian William Vojvodic, Wyatt Carnes

# First we'll import the os module
import os

# Module for reading CSV files
import csv

csvpath = os.path.join("Resources","budget_data.csv")
date = []
revenue = 0
coInfo = []
x = 0
pftCh = []
bkPft = float(0)
bkLss = float(0)
diff = 0
sm=0



with open(csvpath, newline='') as csvfile:
    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")
    # coInfo = list(csvreader)
    for row in csvreader:
        date.append(row[0])
        coInfo.append(row[1])
        revenue = revenue + int(row[1])
    for x in range(1,len(coInfo)):
        diff = int(coInfo[x]) - int(coInfo[x - 1])
        sm=diff+sm
        pftCh.append((diff))
        bkPft = max(pftCh)
        pftCh.index(max(pftCh))
        bkLss = (min(pftCh))
        chAvg = int(sm) / (len(coInfo)-1)  
print("Financial Analysis \n------------------------------")
print(f"Total Months: {len(date)}")
print(f"Total: ${revenue}")
print(f"Average Change: {round(chAvg,2)}")
print(f"Greatest Increase in Profits: {date[(pftCh.index(max(pftCh))+1)]} ${ (bkPft)}")
print(f"Greatest Decrease in Profits: {date[(pftCh.index(min(pftCh))+1)]} ${ (bkLss)}")


# Specify the file to write to
output_path = os.path.join("PyBank", "new.txt")

# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w', newline='') as csvfile:

    # Initialize csv.writer
    csvwriter = csv.writer(csvfile, delimiter=',')

    csvwriter.writerow(["Financial Analysis"])
    csvwriter.writerow(["------------------------------"])
    csvwriter.writerow([f"Total Months: {len(date)}"])
    csvwriter.writerow([f"Total: ${revenue}"])
    csvwriter.writerow([f"Average Change: {round(chAvg,2)}"])
    csvwriter.writerow([f"Greatest Increase in Profits: {date[(pftCh.index(max(pftCh))+1)]} ${ (bkPft)}"])
    csvwriter.writerow([f"Greatest Decrease in Profits: {date[(pftCh.index(min(pftCh))+1)]} ${ (bkLss)}"])