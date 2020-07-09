#import modules
import csv
import os

#Files to Load/Output
file_to_load = os.path.join("Resources", "election_data.csv")
output_path =os.path.join("analysis", "election_analysis.txt")  

#variables
total_votes = 0 
xvotes = 0

#lists
candidates = {}
VoteWinner = {}

#Read
with open(file_to_load) as election_data:
        reader = csv.reader(election_data)

        #header
        header = next(reader)

        for row in reader:
            total_votes += 1 #get total number of votes

            name = row[2] #get candidates name

            if name not in candidates:
                #add name in vote_count
                candidates[name] = 1

            else: 
                #increment the vote count    
                candidates[name] = candidates[name] + 1

print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")

for candidate_name, vote_count in candidates.items(): 
        percentage = (vote_count / total_votes) * 100                   #percentage calucation
        print(f"{candidate_name}: {percentage:,.3f}%, {vote_count}")    #clean table
        
        if candidate_name not in VoteWinner:
            VoteWinner[candidate_name] = vote_count  

print("-------------------------")

for candidate_name_3, vote_count2 in VoteWinner.items(): #running an if/then on this dictionary
    if vote_count2 > xvotes:
        xvotes = vote_count2
    # else: 
    #     print(f"{xvotes}")                #proof this if/then logic is valid
    #     print("loser")                    #highest vote count sticks, three losers!

        if xvotes == vote_count2:
            winner = candidate_name_3       
            print(f"Winner: {str(winner)}")  #prints winner out on the bottom!

print("-------------------------")

#Thank you to instructor Dom for help on lines 1-33 and lines 40-42  
#I have added some minor tweaks to get the correct outputs based on the framework he provided.  

   #write 
with open(output_path, 'w') as csvfile:
   csvwriter = csv.writer(csvfile, delimiter=",")
   csvwriter.writerow(["Election Results"])
   csvwriter.writerow(["Total Votes:", total_votes])
   csvwriter.writerow(candidates.items())
   csvwriter.writerow(["Winner:", winner])

