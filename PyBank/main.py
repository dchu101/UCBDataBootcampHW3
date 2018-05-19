#redo with zip() function?

# zip converts multiple list into tuples

# Import files into list.

import csv

budget_data = []

#CSV importer
def importCSV(filename):
    with open(filename) as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')

        #skip headerline
        next(csvreader)

        for row in csvreader:

            budget_data.append(row)
    
#import CSVs
importCSV('budget_data_1.csv')
importCSV('budget_data_2.csv')

#Normalizing the date into YY-MM format
for row in range(len(budget_data)):

    #shorten YYYY to YY, change MON to MM, then swap two values to sort properly
    month = budget_data[row][0].replace('-20','-').replace('Jan','01').replace('Feb','02').replace('Mar','03').replace('Apr','04').replace('May','05').replace('Jun','06').replace('Jul','07').replace('Aug','08').replace('Sep','09').replace('Oct','10').replace('Nov','11').replace('Dec','12')
    month = month.split('-')
    newMonth = str(month[1]) + '-' + str(month[0]) 
    budget_data[row][0] = newMonth

#Sorts the budget data by the YY-MM date
budget_data = sorted(budget_data)

#month count and revenue aggregation
revenue_total = int(budget_data[0][1])
month_name = budget_data[0][0]
monthly_revenue = int(budget_data[0][1])
#list variable to hold month_name + monthly_revenue
months =[]

for row in range(1,len(budget_data)):

    if str(budget_data[row][0]) == str(budget_data[row-1][0]):
        monthly_revenue += int(budget_data[row][1])
    
    elif str(budget_data[row][0]) != str(budget_data[row-1][0]):
        current_month = [month_name,monthly_revenue]
        months.append(current_month)
        month_name = budget_data[row][0]
        monthly_revenue = int(budget_data[row][1])

    revenue_total += int(budget_data[row][1])

#captures last month, not captured above
current_month = [month_name,monthly_revenue]
months.append(current_month)

#find max and min values for revenue change
best_month = months[0][0]
best_month_amt = months[0][1]
worst_month = months[0][0]
worst_month_amt = months[0][1]

for row in range(1, len(months)):

    if months[row][1] > best_month_amt :
        best_month = months[row][0]
        best_month_amt = months[row][1]
    elif months[row][1] < worst_month_amt :
        worst_month = months[row][0]
        worst_month_amt = months[row][1]   

file = open("output.txt","w+")

file.write('Financial Analysis\n')
file.write('----------------------------\n')
file.write('Total months: ' + str(len(months))+'\n')
file.write('Average revenue change: $' + str(round(revenue_total/len(months), 2))+'\n')
file.write('Greatest Increase in Revenue: 20' + best_month + ' ($' + str(round(best_month_amt, 2)) + ')\n')
file.write('Greatest Decrease in Revenue: 20' + worst_month + ' ($' + str(round(worst_month_amt, 2)) + ')\n')

file = open("output.txt","r")

for row in file:
    print(row)

file.close()