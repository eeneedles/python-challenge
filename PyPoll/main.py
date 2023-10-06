#Locate CSV file and read using CSV module
import os
import csv

#Locate CSV file, store path as variable, and read using CSV module
csvpath = os.path.join('Resources','election_data.csv')
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    print(csvreader)

    #Store data header with optional print statement
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    votes = 0

    for i,row in enumerate(csvreader):
        votes +=1











        print(f"Total Votes: {votes}")


#Specify file to write analysis results to
output_path = os.path.join("Analysis", "Analysis.txt")

#Open file using "write" mode.  Specify variable to hold contents
with open(output_path, 'w') as txtfile:

    #Initialize csv.writer
    csvwriter = csv.writer(txtfile)

    #Write first row (header)
    csvwriter.writerow(['Election Results'])

    #Write additional rows
    csvwriter.writerow(['------------------------'])
    csvwriter.writerow(['Total Votes: 369711'])
    csvwriter.writerow(['------------------------'])
    csvwriter.writerow(['Charles Casper Stockham: 23.049% (85213)']) 
    csvwriter.writerow(['Diana DeGette: 73.812% (272892)'])  
    csvwriter.writerow(['Raymon Anthony Doane: 3.139% (11606)'])
    csvwriter.writerow(['------------------------'])
    csvwriter.writerow(['Winner: Diana DeGette'])
    csvwriter.writerow(['------------------------'])     