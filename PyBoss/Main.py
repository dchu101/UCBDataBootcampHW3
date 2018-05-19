# Import files into list.
# Create index length of the employee data.
# Split the name column into first and last name.
# Split the date on delimiter, then reassemble with new delimiter, convert from YYYY-MM-DD to MM/DD/YYYY
# Split the date on SSN, delimiter '-', take ssn[2] and append last 4 digits to ****-**-
# Convert state to abbrev
# put all converted values in list, add to new data list
# write everything in CSV

import csv

#os.path.join('..', 'output', 'new.csv')
# ../output/new.csv

old_employee_data = []

#CSV importer
def importCSV(filename):
    with open(filename) as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')

        #skip headerline
        next(csvreader)

        for row in csvreader:

            old_employee_data.append(row)

#import CSVs
importCSV('employee_data1.csv')
importCSV('employee_data2.csv')

index = len(old_employee_data)

us_state_abbrev = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY',
}

#create new list for employee data
new_employee_data = [['Emp ID', 'First Name', 'Last Name', 'DOB', 'SSN', 'State']]
new_column_index = len(new_employee_data[0])

#append each employee record and add to new_employee_data
for row in range(index):
    employee_id = old_employee_data[row][0]
    splitName = old_employee_data[row][1].split(' ')
    first_name = splitName[0]
    last_name = splitName[1]
    split_dob = old_employee_data[row][2].split('-')
    new_dob = split_dob[1] + '/' + split_dob[2] + '/' + split_dob[0]
    split_ssn = old_employee_data[row][3].split('-')
    new_ssn = '****-**-' + split_ssn[2]
    old_state = old_employee_data[row][4]
    new_state = us_state_abbrev.get(old_state)
    new_employee_data.append([employee_id, first_name, last_name, new_dob, new_ssn, new_state])


file = open("output.csv", "w+")

#index+1 because there's header row here, so all values get moved up one
for row in range(index+1):
    for column in range(new_column_index-1):
        file.write(str(new_employee_data[row][column]) + ',')
    file.write(str(new_employee_data[row][new_column_index-1]) + '\r\n')

file.close()