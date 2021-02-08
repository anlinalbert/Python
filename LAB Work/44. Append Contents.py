# Append user input to file

filename = input("Enter filename: ")

with open(filename, 'a') as f:
    f.write(input())

f.close()