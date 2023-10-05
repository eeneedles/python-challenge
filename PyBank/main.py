import os
import csv

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

    for i,row in enumerate(csvreader):
        # print(row)
        # months = months + 1
        months +=1
        profit_loss = int(row[1])
        net_total +=profit_loss

        if i > 0:
            
            change = profit_loss - previous
            changes.append(change)
            previous = profit_loss
        else:
            previous = profit_loss
        
    print(months)
    print(f"Net Total: ${net_total}")
    
    


