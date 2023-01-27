# reading a csv file through Python 

import csv 
from dataclasses import field
with open('csv_sample.csv') as f: 
    csv_reader = csv.reader(f, delimiter=',') # reader method to read the csv file
    line_count = 0 
    for row in csv_reader: 
        if line_count == 0:
            print(f'Column names are: {", ".join(row)}')
            line_count += 1
        else: 
            print(f'\t{row[0]} is a teacher.He lives in {row[1]}, {row[2]}.')
            line_count += 1
    print(f'Number of lines: {line_count}')


# writing to a csv file through Python 

import csv 

cols = ['Name','Branch','Year','Skills']

rows =  [ ['Nelson', 'COE', '2020', 'javascript'],
          ['Susan', 'Cloud', '2021', 'AWS'],
          ['Alan', 'IT', '2019', 'VMware'],
          ['Matt', 'COE', '2018', 'Azure'] ]

filename = "employee_records.csv"

# writing to the csv file 

with open(filename, 'w') as csvfile:
    csvwriter = csv.writer(csvfile)

# writing the fields 

csvwriter.writerow(cols)

# writing the data rows 
csvwriter.writerows(rows)
csvfile.close()


