# Import files into list.
# Then, run through all data to identify unique candidates in list.
# Create index = length of candidates.
# Create corresponding vote total lists, use candidate index to match position. 
# E.g. candidateList[3] corresponds to voteTotal[3].
# Calculate winner based on max of the voteTotal.
# Calculate totalVotes based on length of raw data.
# Use voteTotal and totalVotes to create another indexed votePercentage list.
# Write output to file, read file in terminal.

import csv

poll_data = []

#CSV importer
def importCSV(filename):
    with open(filename) as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')

        #skip headerline
        next(csvreader)

        for row in csvreader:

            poll_data.append(row)

#import CSVs
importCSV('election_data_1.csv')
importCSV('election_data_2.csv')


#this populates candidate list
candidateList = [poll_data[0][2]]
for row in range(len(poll_data)):

    if poll_data[row][2] not in candidateList:
        candidateList.append(poll_data[row][2])

#index is variable based on position in candidate list, matches to corresponding voteCount and votePercentage
index = len(candidateList)

#this populates a list with equal length to candidateList, populated with 0 (blank slank vote tally)
totalVotes = len(poll_data)
voteCount=[]

for row in range(index):
    voteCount.append(0)

#this tallies votes, with voteCount indexed against candidateList position

for row in range(0,len(poll_data)):

    voteCount[candidateList.index(poll_data[row][2])] += 1

#this calculates the winner

winningVoteCount = max(voteCount)
winningCandidate = candidateList[voteCount.index(winningVoteCount)]

#total votes

# list containing vote % calculations

votePercentage = []
for row in range(index):
    votePercentage.append(round(100 * voteCount[row] / totalVotes, 2))

#Output file, then read-write file to terminal
file = open("output.txt","w+")

file.write('Election results\n')
file.write('-------------------------\n')
file.write('Total votes: ' + str(totalVotes) +'\n')
file.write('-------------------------\n')

for row in range(len(candidateList)):
    file.write(str(candidateList[row]) + ': ' + str(votePercentage[row]) + '% (' + str(voteCount[row]) + ')\n')

file.write('-------------------------\n')

file.write('Winner: ' + str(winningCandidate) + '\n')

file.write('-------------------------')

file = open("output.txt","r")

for row in file:
    print(row)

file.close()