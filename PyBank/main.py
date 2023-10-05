#Import os and csv modules for creating file paths across operating systems and reading csv files
import os
import csv

#Locate csv file and read using CSV module
csvpath = os.path.join('Resources','budget_data.csv')
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    print(csvreader)
 
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    months = 0
    net_total = 0
    changes = []
    previous = 0

    #Calculate total number of months, net total amount of profit/losses over period
    for i,row in enumerate(csvreader):
        # print(row)
        # months = months + 1
        months +=1
        profit_loss = int(row[1])
        net_total +=profit_loss

        #Calculate changes in profit/losses over period
        if i > 0:
            
            change = profit_loss - previous
            changes.append(change)
            previous = profit_loss
        else:
            previous = profit_loss
    #Create financial analysis dataset displaying month total, net total of profit/losses, average change in profit/losses, and Greatest Increase and Decrease in Profits        
    print(months)
    print(f"Total: ${net_total}")

    


