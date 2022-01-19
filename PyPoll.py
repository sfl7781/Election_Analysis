#Add dependencies
import csv
import os

# Assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources", "election_results.csv")

#Assign a variable for file name in the Analysis folder
file_to_save=os.path.join("Analysis", "election_analysis.txt")

# Initialize total vote counter
total_votes = 0

#Candidate options list
candidate_options = []
#Candidate votes list
candidate_votes = {}

# Winning Candidate and Winning # & %
winning_candidate = ""
winning_count = 0
winning_percentage = 0

#Open the election results and read the file
with open(file_to_load) as election_data:
  file_reader = csv.reader(election_data)  
 
 # Read and print the header row.
  headers = next(file_reader)
   #print(headers)

# Print each row in the CSV file.(must be inside 'with' block)
  for row in file_reader:
    #print(row)     
    total_votes += 1
    # Print the candidate name from each row
    candidate_name = row[2]

  # If candidate is not an existing candidate
    if candidate_name not in candidate_options:
      # Add candidate to the list
      candidate_options.append(candidate_name)
      # initialize candidate vote count at zero
      candidate_votes[candidate_name] = 0

# Add votes to candidate's names
    candidate_votes[candidate_name] += 1
# Save results to text file
with open(file_to_save, "w") as txt_file:
# print the final vote count
  election_results = (
    f"\nElection Results\n"
    f"-------------------------\n"
    f"Total Votes: {total_votes:,}\n"
    f"-------------------------\n")
  print(election_results, end="")
  
  # Save the vote count to text file
  txt_file.write(election_results)

  # the % of votes for each candidate
  # 1. loop through candidate list
  for candidate_name in candidate_votes:
      # 2. vote count of candidate
    votes = candidate_votes[candidate_name]
      # 3. % of votes
    vote_percentage = float(votes) / float(total_votes) * 100

  # 4. Print the candidate name and percentage of votes.
    candidate_results = (f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n\n")

  #  Save the candidate results to our text file.
    txt_file.write(candidate_results)  


  # Determines winning vote count,candidate & %
    if (votes > winning_count) and (vote_percentage > winning_percentage):
      # If true then: 
      winning_count = votes
      winning_percentage = vote_percentage
      winning_candidate = candidate_name

  winning_candidate_summary = (
      f"-------------------------\n"
      f"Winner: {winning_candidate}\n"
      f"Winning Vote Count: {winning_count:,}\n"
      f"Winning Percentage: {winning_percentage:.1f}%\n"
      f"-------------------------\n")

  print(winning_candidate_summary)
  # Write the winning candidate's results to the text file
  txt_file.write (winning_candidate_summary)





# 4. Print the candidate name and percentage of votes.
# print(f"{candidate_name}: received {vote_percentage:.1f}% of the vote.")



# Print candidate votes
#print(candidate_votes)

#Print the candidate list
#print(candidate_options)

# Print total votes
#print(total_votes)
