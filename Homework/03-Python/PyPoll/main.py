import os
import csv

# Path to collect data from the Resources folder
py_poll_csv = os.path.join('.', 'Resources', 'PyPoll_election_data.csv')

def get_voting_data():
    # Open the CSV
    # Read through csv file
    with open(py_poll_csv, 'r') as pyPollCSVFile:
        total_votes = 0
        khan_total_vote_array = []
        khan_total_votes = 0
        khan_percent = 0
        correy_total_vote_array = [] 
        correy_total_votes = 0
        correy_percent = 0 
        li_total_votes = 0
        li_percent = 0
        li_total_vote_array = []
        otooley_total_votes = 0
        otooley_percent = 0
        otooley_total_vote_array = []
        voter_id_array = [] 
        candidates = ["Khan", "Correy", "Li","O'Tooley"]
        votes = [khan_total_votes, correy_total_votes,li_total_votes,otooley_total_votes]

        # Split the data on commas
        csv_reader = csv.reader(pyPollCSVFile, delimiter=',')
        header = next(csv_reader)

        for data in csv_reader:
            voter_id_array.append(data[0])
            total_votes = len(voter_id_array)

            if data[2] == "Khan":
                khan_total_vote_array.append(data[2])
                khan_total_votes = len(khan_total_vote_array)
                khan_percent = round((khan_total_votes / total_votes) * 100, 2)
            if data[2] == "Correy":
                correy_total_vote_array.append(data[2])
                correy_total_votes = len(correy_total_vote_array)
                correy_percent = round((correy_total_votes / total_votes) * 100, 2)
            if data[2] == "Li":
                li_total_vote_array.append(data[2])
                li_total_votes = len(li_total_vote_array)
                li_percent = round((li_total_votes / total_votes) * 100, 2)
            if data[2] == "O'Tooley":
                otooley_total_vote_array.append(data[2])
                otooley_total_votes = len(otooley_total_vote_array)
                otooley_percent = round((otooley_total_votes / total_votes) * 100, 2)
            
            dict_candidates_and_votes = dict(zip(candidates,votes))
            key = max(dict_candidates_and_votes, key=dict_candidates_and_votes.get)

    # Print to Terminal     
    print("Election Results")       
    print("----------------------------")
    print(f"Total Votes: {total_votes}")
    print("----------------------------")
    print(f"Khan: {khan_percent}% ({khan_total_votes})")
    print(f"Correy: {correy_percent}% ({correy_total_votes})")
    print(f"Li: {li_percent}% ({li_total_votes})")
    print(f"O'Tooley: {otooley_percent}% ({otooley_total_votes})")
    print("----------------------------")
    print(f"Winner: {key}")
    print("----------------------------")

    # Write to text file  
    file1 = open("./analysis/results.txt","w")
    file1.write("Election Results\n")       
    file1.write("----------------------------\n")
    file1.write(f"Total Votes: {total_votes}\n")
    file1.write("----------------------------\n")
    file1.write(f"Khan: {khan_percent}% ({khan_total_votes})\n")
    file1.write(f"Correy: {correy_percent}% ({correy_total_votes})\n")
    file1.write(f"Li: {li_percent}% ({li_total_votes})\n")
    file1.write(f"O'Tooley: {otooley_percent}% ({otooley_total_votes})\n")
    file1.write("----------------------------\n")
    file1.write(f"Winner: {key}\n")
    file1.write("----------------------------\n")

get_voting_data()