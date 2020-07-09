import os
import csv

csvpath = os.path.join('Resources', 'budget_data.csv')

with open(csvpath) as csvfile:
   csvreader = csv.reader(csvfile, delimiter=",")
   next(csvreader) #skip header

   Months = 0
   ProfitTotal = 0 #set a variable outside the loops
   
   MonthlyChange = 0 
   PS = 0 #Profit Start
   PL = 0 #Profits/Losses
   MC = 0 #MonthlyChange Sum Holder
   AverageChange = 0

   GI = 0 
   GD = 0
   

   for row in csvreader:
      Months += 1 #count months

      PS = int(row[1])  #Get Profit For Month
      ProfitTotal += PS #Calculate Total

      MonthlyChange = (PS - PL) #Get Difference in Monthly Change
      if MonthlyChange > GI: #Keep Greatest Increase
         GI = MonthlyChange
         GIM = str(row[0]) #Keep Date as String

      if MonthlyChange < GD: #Keep Greatest Decrease
         GD = MonthlyChange 
         GDM = str(row[0]) #Keep Date as String

      MC += MonthlyChange #Calculate a Total Monthly Change Figure
         
      PL = PS #Use PL as a placeholder to calculate Monthly Change

   AverageChange = (MC - 867884) / (Months - 1)
      #CHANGE 867884 VAlUE WITH DATA SET, CAN'T GET RID OF OFF BY 1 ERROR


   #print
   print("Financial Analysis")
   print("----------------------------")
   print(f"Total Months: {Months}")
   print(f"Total: ${ProfitTotal:,.2f}")
   print(f"Average Change: ${AverageChange:,.2f}")
   print(f"Greatest Increase in Profits: {GIM} ${GI:,.2f}")
   print(f"Greatest Decrease in Profits: {GDM} ${GD:,.2f}")

   #write
file_to_output = os.path.join("analysis", "FinancialAnalysis.csv")

with open(file_to_output, 'w') as csvfile:
   csvwriter = csv.writer(csvfile, delimiter=',')
   
   csvwriter.writerow(["Financial Analysis"])
   csvwriter.writerow(["Total Months:", Months])
   csvwriter.writerow(["Total: $", ProfitTotal])
   csvwriter.writerow(["Average Change: $", AverageChange])
   csvwriter.writerow(["Greatest Increase in Profits: $", GI])
   csvwriter.writerow(["Greatest Decrease in Profits: $", GD])