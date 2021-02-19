# Write a Python program to read each row from a given csv file and print a list of
# strings.

import csv

with open('D:\MCA\Sem 1\Python\LAB Work\myfile.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)
file.close()