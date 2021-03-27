#PyPoll


#Modules
import os
import csv

#csv read
csvpath = os.path.join("Resources", "election_data.csv")

with open (csvpath) as csvfile:
    
    csvreader = csv.reader(csvfile, delimiter=',')

    csv_header = next(csvreader)

    #start vars
    total_votes = 0
    candidate_list = []
    candidate_votes = []
    candidate_percentage = []

    #get total votes and candidate list 
    for row in csvreader:

        #find total votes
        total_votes = total_votes + 1

        if row[2] not in candidate_list:
            candidate_list.append(row[2]) 
            candidate_votes.append(1)
        else:
            index = int(candidate_list.index(row[2]))
            candidate_votes[index] +=1

    #calculate percentage list
    i = 0
    percentage = 0
    while i < len(candidate_votes):
        percentage = float((candidate_votes[i] / total_votes)*100)
        candidate_percentage.append(percentage)
        i += 1

# print results
print(f"Election Results")
print(f"----------------")
print(f"Total Votes: {total_votes}")
print(f"----------------")
print(f"{candidate_list[0]}: {candidate_percentage[0]} ({candidate_votes[0]}) ")
print(f"{candidate_list[1]}: {candidate_percentage[1]} ({candidate_votes[1]}) ")
print(f"{candidate_list[2]}: {candidate_percentage[2]} ({candidate_votes[2]}) ")
print(f"{candidate_list[3]}: {candidate_percentage[3]} ({candidate_votes[3]}) ")
print(f"----------------")