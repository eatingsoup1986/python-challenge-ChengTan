import os
import csv

pybank_csv = os.path.join("Resources", "budget_data.csv")

#open CSV file
with open(pybank_csv) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")

    #read the header row first
    csv_header = next(csv_file)
    print(f"Header: {csv_header}")
    
    #read through each row of data after the header
    for row in csv_reader:
        print(row)