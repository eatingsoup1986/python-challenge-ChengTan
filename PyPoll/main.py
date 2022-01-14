import os
import csv

# set a csv file path for the data
pypoll_csv = os.path.join('Resources', 'election_data.csv')


# define variables
totalvotes = 0
votes = []
candidatecount = []
candidates = []
percent = []

with open(pypoll_csv, 'r') as csvfile:
    #split data with commas
    csvreader = csv.reader(csvfile, delimiter=',')
    #CSVS file has headings
    csvheader = next(csvreader)

# start loop of row
    for row in csvreader:
    # count the total votes
        totalvotes += 1
    # append candidate names to a candidates list
        if row[2] not in candidates:
            candidates.append(row[2])
    # list all of the votes
        votes.append(row[2])

# second loop to add to candidate count with each vote
    for candidate in candidates:
        candidatecount.append(votes.count(candidate))
        percent.append(round(votes.count(candidate)/totalvotes*100,3))

# find the winner using index position of the max count in candidate count
    winner = candidates[candidatecount.index(max(candidatecount))]
    
# print results, use a loop for individual candidates
print('Election Results')
print('--------------------------------')
print(f'Total Votes: {totalvotes}')
print('--------------------------------')
for i in range(len(candidates)):
    print(f'{candidates[i]}: {percent[i]}% ({candidatecount[i]})')
print('--------------------------------')
print(f'Winner: {winner}')
print('--------------------------------')

# save summary output to txt file

save_file = pypoll_csv.strip(".csv") + "_analysis.txt"
filepath = os.path.join(".", save_file)
    
with open(filepath,'w') as f:
    f.write('Election Results')
    f.write('\n------------------------------------')
    f.write(f'\nTotal Votes: {totalvotes}')
    f.write('\n------------------------------------')
    for i in range (len(candidates)):
        f.write(f'\n{candidates[i]}: {percent[i]}% {candidatecount[i]}')
    f.write('\n------------------------------------')
    f.write(f'\nWinner: {winner}')
    f.write('\n------------------------------------')