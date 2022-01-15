#Add dependencies
import csv
import os

# Assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources", "election_results.csv")

#Assign a variable for file name in the Analysis folder
file_save=os.path.join("Analysis", "election_analysis.txt")

#Open the election results and read the file
with open(file_to_load) as election_data:
  file_reader = csv.reader(election_data)  
 
 # Read and print the header row.
  headers = next(file_reader)
  print(headers)

# Print each row in the CSV file.(must be inside 'with' block)
  for row in file_reader:
    print(row)     
