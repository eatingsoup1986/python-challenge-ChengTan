import os
import csv

#path to collect the data
pypoll_csv = os.path.join("Resources", "election_data.csv")


#track variables and parameters
total_votes = 0
candidate_votes = {}
candidate_list = []
max_count = 0
max_candidate_vote = ""

#read in the CSV file
with open(pypoll_csv, 'r') as csvfile:
    #split data with commas
    csvreader = csv.reader(csvfile, delimiter=',')
    #CSVS file has headings
    csvheader = next(csvreader)
    
    #Track total overall
    for row in csvreader:
        total_votes = total_votes + 1
    #Track total for individual candiates
        candidate_name = row[2]

        if candidate_name not in candidate_list:
            candidate_list.append(candidate_name)
            candidate_votes[candidate_name] = 0
        
        candidate_votes[candidate_name] = candidate_votes[candidate_name] + 1           

#cacluations for the votes
    for candidate in candidate_votes:
        votes = candidate_votes.get(candidate)
        percentage_vote = float(votes) / float(total_votes) * 100


        if (votes > max_count):
            max_count = votes
            max_candidate_vote = candidate

# print summary to terminal

    print("Election Results")
    print("---------------------------")
    print(f"Total Votes: {total_votes}")
    print("---------------------------")
    print(f"Candidate Votes: {candidate}: {percentage_vote:.3f}% ({votes})")
    print("---------------------------")
    print(f"Winner: {max_candidate_vote}")

# save summary output to txt file
# reference for future instructions: 
# https://www.pythontutorial.net/python-basics/python-write-text-file/
#save_file = pypoll_csv.strip(".csv") + "_analysis.txt"
#filepath = os.path.join(".", save_file)
#with open(filepath,'w') as f:
#    f.write("Election Results" + '\n')
#    f.write("---------------------------" + '\n')
#    f.write(f"Total Votes: {total_votes}" + '\n')
#    f.write("---------------------------" + '\n')
#    f.write("Khan: " + str(kahn_vote) + '\n')
#    f.write("Correy: " + str(correy_vote) + '\n')
#    f.write("Li: " + str(li_vote) + '\n')
#    f.write("O'Tooley: " + str(otool_vote) + '\n')
#    f.write("---------------------------" + '\n')
#    f.write(f"Winner: {max_candidate_vote}" + '\n')
    