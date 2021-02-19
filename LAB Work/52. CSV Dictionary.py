# Write a Python program to write a Python dictionary to a csv file. After writing
# the CSV file read the CSV file and display the content.

import csv

with open('D:\MCA\Sem 1\Python\LAB Work\myfile.csv', 'w') as f:
    fieldnames = ['Name', 'Department', 'Birthday Month']
    content = csv.DictWriter(f, fieldnames = fieldnames)
    content.writeheader()
    content.writerow({'Name': 'John', 'Department': 'Accounting', 'Birthday Month': 'November'})
    content.writerow({'Name': 'Amy', 'Department': 'IT', 'Birthday Month': 'March'})
f.close()

with open('D:\MCA\Sem 1\Python\LAB Work\myfile.csv', 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)
f.close()