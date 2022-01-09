import os
import csv

#path to collect the data
pybank_csv = os.path.join("Resources", "budget_data.csv")


#track variables and parameters
total_months = 0
revenue = 0
last_revenue = 0
revenue_change = 0
revenue_changes = []
months = []
average_change = []
greatest_increase = ["", 0]
greatest_decrease = ["", 99999999999999999999]
total_revenue = 0

#read in the CSV file
with open(pybank_csv, 'r') as csvfile:
    #split data with commas
    csvreader = csv.reader(csvfile, delimiter=',')
    #CSVS file has headings
    csvheader = next(csvreader)
    
    #Track totals
    for row in csvreader:
        total_months = total_months + 1
        months.append(row[0])
        revenue = int(row[1])
        total_revenue = total_revenue + revenue
        if total_months > 1:
            revenue_change = revenue - last_revenue
            revenue_changes.append(revenue_change)
        last_revenue = revenue

#cacluations for month to month
    max_change = max(revenue_changes)
    min_change = min(revenue_changes)
    sum_revenue_changes = sum(revenue_changes)
    average_change = round(sum_revenue_changes / (total_months - 1),2)
    max_month_value = revenue_changes.index(max_change)
    min_month_value = revenue_changes.index(min_change)
    max_month = months[max_month_value + 1]
    min_month = months[min_month_value + 1]
# print summary

    print("Financial Analysis")
    print("---------------------------")
    print(f"Total Months: {total_months}")
    print("Total: $" + str(total_revenue))
    print(f"Average Change: ${average_change}")
    print(f"Greatest Increase in Profits: {max_month} (${max_change})")
    print(f"Greatest Decrease in Profits: {min_month} (${min_change})")

# save summary output to txt file
# reference for future instructions: 
# https://www.pythontutorial.net/python-basics/python-write-text-file/
save_file = pybank_csv.strip(".csv") + "_analysis.txt"
filepath = os.path.join(".", save_file)
with open(filepath,'w') as f:
    f.write("Financial Analysis" + "\n")
    f.write("---------------------------" + "\n")
    f.write(f"Total Months: {total_months}" + "\n")
    f.write("Total: $" + str(total_revenue) + "\n")
    f.write(f"Average Change: ${average_change}" + "\n")
    f.write(f"Greatest Increase in Profits: {max_month} (${max_change})" + "\n")
    f.write(f"Greatest Decrease in Profits: {min_month} (${min_change})" + "\n")