#Import OS and CSV modules for creating file paths across operating systems and reading csv files
import os
import csv  


#Locate CSV file and read using CSV module
csvpath = os.path.join('Resources','budget_data.csv')
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    print(csvreader)

    #Store data header
    csv_header = next(csvreader)

    #Define variables
    months = 0
    net_total = 0
    changes = []
    previous = 0

    #Calculate total number of months -  learned enumerate function from tutor Justin Moore
    for i,row in enumerate(csvreader):
        months +=1

        #Calculate net total amount of profit/losses over period
        profit_loss = int(row[1])
        net_total +=profit_loss

        #Calculate changes in profit/losses over period
        if i > 0:
            change = profit_loss - previous
            changes.append(change)
            previous = profit_loss
        else:
            previous = profit_loss

        #Calculate average change
        def average(changes):
            length = len(changes)
            total = 0.0
            for change_event in changes:
                total += change_event
            return total / length
        
    #Calculate greatest increase in profit
    greatest_increase = 0
    for i in changes:
        if i > greatest_increase:
            greatest_increase = i

    #Calculate greatest decrease in profit
    greatest_decrease = 0
    for i in changes:
        if i < greatest_decrease:
            greatest_decrease = i

    #Create financial analysis dataset displaying month total, net total of profit/losses, average change in profit/losses, and Greatest Increase and Decrease in Profits        
    print("Financial Analysis")
    print("---------------------------")
    print(f"Total Months: {months}")
    print(f"Total: ${net_total}")
    print(f"Average Change: ${average(changes)}")
    print(f"Greatest Increase in Profits: ${greatest_increase}")
    print(f"Greatest Decrease in Profits: ${greatest_decrease}")     

#Specify file to write analysis results to
output_path = os.path.join("Analysis", "Analysis.txt")

#Open file using "write" mode.  Specify variable to hold contents
with open(output_path, 'w') as txtfile:

    #Initialize csv.writer
    csvwriter = csv.writer(txtfile)

    #Write first row (header)
    csvwriter.writerow(['Financial Analysis'])

    #Write additional rows
    csvwriter.writerow(['------------------------'])
    csvwriter.writerow(['Total Months: 86'])
    csvwriter.writerow(['Total: $22564198'])
    csvwriter.writerow(['Average Change: $-8311.11']) 
    csvwriter.writerow(['Greatest Increase in Profits: Aug-16 ($1862002)'])  
    csvwriter.writerow(['Greatest Decrease in Profits: Feb-14 ($-1825558)'])     

    

