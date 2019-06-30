# Homework completed by Mohammad Zahid Shiwani, Adrian William Vojvodic, Wyatt Carnes

# First we'll import the os module
import os

# Module for reading CSV files
import csv
# election_data.csv
# joining the path
csvpath = os.path.join("Resources","election_data.csv")

# Defining variables, lists and dictionary
# list of all entries
cand = []
# dictionary explaining no of votes for each candidate 
cand_data = {}
# total no of votes counter
total_votes = 0
# Extraction of dictionary keys
cand_vote = []
# extracction of dictionary values 
cand_name = []

# open csv file
with open(csvpath, newline='') as csvfile:
    # CSV reader specifies delimiter and variable that holds contents
    election_Data = csv.reader(csvfile, delimiter=',')
    # Read the header row first (skip this step if there is now header)
    csv_header = next(election_Data)
    
    # list of votes for all candidates 
    for row in election_Data:
        cand.append(row[2])
    # Filling in the dictionary 
    for a in cand:
        if a not in cand_data:
            cand_data[a] = 1
        else:
            cand_data[a] += 1
        total_votes = total_votes + 1
        
    for key, value in cand_data.items():
        cand_name.append(key)
        cand_vote.append(value)
    # Alternate 
    # for row in election_Data:
    #     if row[2] not in cand_data:
    #         cand_data[row[2]] = 1
    #     else:
    #         cand_data[row[2]] += 1
    #     total_votes = total_votes + 1
        
# print(cand_data)
# print(total_votes)
# print(cand_name)
# print(cand_vote)
# print(max(cand_vote))

pctV = [(a*100) / total_votes for a in (cand_vote)]
#     #print(pctV)
#     wins = cand_nm[pctV.index(max(pctV))]
#     #print(wins)
print("Election Results \n------------------------------")
print(f"Total Votes: {total_votes} \n------------------------------")
for i in range(len(cand_name)):
    print(f"{cand_name[i]}: {round(pctV[i],3)}% ({cand_vote[i]})")
print(f"------------------------------\n Winner: {cand_name[cand_vote.index(max(cand_vote))]}\n------------------------------")

# Specify the file to write to
output_path = os.path.join("PyPoll", "new.txt")

# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w', newline='') as csvfile:

    # Initialize csv.writer
    csvwriter = csv.writer(csvfile, delimiter=',')

    csvwriter.writerow(["Election Results"])
    csvwriter.writerow(["------------------------------"])
    csvwriter.writerow([f"Total Votes: {total_votes}"])
    csvwriter.writerow(["------------------------------"])
    for i in range(len(cand_name)):
        csvwriter.writerow([f"{cand_name[i]}: {round(pctV[i],3)}% ({cand_vote[i]})"])
    csvwriter.writerow(["------------------------------"])
    csvwriter.writerow([f"Winner: {cand_name[cand_vote.index(max(cand_vote))]}"])
    csvwriter.writerow(["------------------------------"])
    