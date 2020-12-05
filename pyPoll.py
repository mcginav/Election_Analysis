#The data we need to retrieve.
#1. Total number of votes cast
#2. Complete list of candidates who received votes
#3. The percentage of votes each candidate won
#4. The total number of votes each candidate won
#5. The winner of the election based on popular vote.

# Add dependencies.
import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Open the election results and read the file
election_data = open(file_to_load,'r')

#1. Initialize a total vote counter
total_votes=0

# Candidate Options
candidate_options = []
#1. Declare the empty dictionary
candidate_votes = {}
#candidate_votes={"candidate_name1":votes, "candidate_name2":votes,"candidate_name3":votes}
#Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open the election results and read the file
with open(file_to_load) as election_data:
    
   # To do: read and analyze the data here.
    file_reader = csv.reader(election_data)

    # Read the header row.
    headers = next(file_reader)
    
    # Print each row in the CSV file.
    for row in file_reader:
        # Add to the total vote count.
        total_votes += 1

    # Print the candidate name from each row    
        candidate_name = row[2]
                
        # If the candidate does not match any existing candidate
        if candidate_name not in candidate_options:
                
        # Add the candidate name to the candidate list
            candidate_options.append(candidate_name)
        #2. Begin tracking that candidate's vote count.    
            candidate_votes[candidate_name] = 0
    # Add a vote to that candidate's count.
        candidate_votes[candidate_name] += 1

    # Save the results to text file
    with open(file_to_save,"w") as txt_file: 
        # Print the final vote coun to the terminal.
            election_results = (
                f"\nElection Results\n"
                f"------------------\n"
                f" Total Votes: {total_votes:,}\n"
                f"------------------\n")
            print(election_results, end="") 
            # Save the final vote count to the text file.
            txt_file.write(election_results)     
            
        # Determine the percentage of votes for each candidate by looping through the counts
        # Iterate through the candidate list.
            for candidate_name in candidate_votes:
                # Retrieve vote count of a candidate.
                votes = candidate_votes[candidate_name]
                # Calculate the percentage of votes.
                vote_percentage = float(votes)/float(total_votes)* 100

                # Print out each candidate's name, vote count, and percentage of votes
                candidate_results = (f"{candidate_name}:{vote_percentage:.1f}% ({votes:,})\n")
                print(candidate_results)
                # Save the candidate results to our text file.
                txt_file.write(candidate_results)

                # Determine winning vote count and candidate
                # Determine if the votes are greater than the winning count.
                if (votes > winning_count) and (vote_percentage > winning_percentage):
                # If true, then set winning_count = votes and winning_percent = # of vote_percentage.
                        winning_count = votes
                        winning_percentage = vote_percentage
                # Set the winning_candidate equal to the candidate's name.
                        winning_candidate = candidate_name

            # Print the winning candidate, vote count, and percentage of votes.
            winning_candidate_summary =(
                f"---------------------\n"
                f"Winner:{winning_candidate}\n"
                f"Winning Vote Count: {winning_count:,}\n"
                f"Winning Percentage: {winning_percentage:.1f}%\n"
                f"---------------------\n")  
                
        # print(f"{candidate_name}: received {vote_percentage:.1f}% of the vote.")  
        # print(winning_candidate_summary) 
        # Print the candidate list.
        # print (candidate_votes)    
            print(winning_candidate_summary)
            #Save the winning candidate's name to the text file
            #txt_file.write(winning_candidate_summary)