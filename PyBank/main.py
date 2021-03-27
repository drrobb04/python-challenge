#PyBank

#Modules
import os
import csv

#csv read
csvpath = os.path.join("Resources", "budget_data.csv")

with open (csvpath) as csvfile:
    
    csvreader = csv.reader(csvfile, delimiter=',')

    csv_header = next(csvreader)

    #start vars
    total_months = 0
    total_pl = 0
    previous_pl = 867884
    changeList = []
    greatest_increase = 0
    greatest_decrease = 0
    greatest_increase_month = ""
    greatest_decrease_month = ""

    for row in csvreader:

        #find total months
        total_months = total_months + 1

        #find total_pl
        total_pl = total_pl + int(row[1])

        #find average change
        current_pl = int(row[1])
        change = current_pl - previous_pl
        previous_pl = int(row[1])
        changeList.append(change)
        average_change = sum(changeList) / len(changeList)
        average_change = round(average_change, 2)

        #find largest increase
        if change > greatest_increase:
            greatest_increase = change
            greatest_increase_month = str(row[0])   

        #find largest decrease
        if change < greatest_decrease:
            greatest_decrease = change
            greatest_decrease_month = str(row[0])  


#print results to terminal
print("Financial Analysis")
print("------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${total_pl}")
print(f"Average Change: ${average_change}")
print(f"Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase})")
print(f"Greatest Decrease in Profits: {greatest_decrease_month} (${greatest_decrease})")

#print results to txt file
output_path = os.path.join("Output", "Results.txt")

