# Write a Python program to read specific columns of a given CSV file and print
# the content of the columns.

import csv

# list of columns to read
included_cols = [0, 1]

with open('D:\MCA\Sem 1\Python\LAB Work\csv read_2.csv', 'r') as f:
    reader = csv.reader(f, delimiter = ',')
    print('Reading only column 1 & 2:\n')
    for row in reader:
        content = list(row[i] for i in included_cols)
        print(content)
f.close()