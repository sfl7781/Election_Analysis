# Election Analysis
## Overview of Election Audit
I have been tasked with helping Tom, an employee for the Colorado Board of Elections. Tom is handling an election audit on a congressional precinct in the state. Thus far we have calculated and submitted various metrics; total number of votes, list of candidates and their assigned votes, the percentage of overall votes each candidate received along with the winning candidate. In order to complete the audit the election commission has requested some additional information:
- The votes tallied for each county
- The percentage of overall votes from each county
- The county with the highest voter turnout
 
### Methodology
1. Data used: election_results.csv; CSV file was supplied and included Ballot ID(used to sum votes), County and Candidate Name 
2. Python 3.10.1 was used to import the csv file and write the code
3. Code was written to automate metrics requested in 'Overview' and outputted into a text file for easier consumption of results.
#### [View code](PyPoll_Challenge.py.md)

## Election Audit Results
***County***
 - **Total Votes Cast** - ***369,711***
 
 - Votes by County and % of overall votes received.
   - **Jefferson 10.5%** (*38,855*)
   - **Denver 82.8%** (*306,055*)
   - **Arapahoe 6.7%** (*24,801*)
 
 - **Denver County** received the most votes

***Candidates***
- Votes by Candidate and % of overall votes received.
  - **Charles Casper Stockham 23%** (*85,213*)
  - **Diana DeGette 73.8%** (*272,892*)
  - **Raymon Anthony Doane 3.1%** (*11,606*)

- *Winning Candidate*
  - ***Diana DeGette*** with ***73.8%*** of the votes
    - She received ***272,892*** of the overall votes
#### [Election Results](Analysis/election_results.txt)

## Election Audit Summary
   Since the code was written to directly pull from the csv file used, this script can be 
interchangeable with essentially any location that provides the same type of data.
Furthermore it can be modified for data that includes demographics such as age, gender, ethnicity, 
religion or education with some adjustment to the assigned variables. This could assist with
statistical analysis while possibly enhancing the campaign strategies of existing
and future candidates.
