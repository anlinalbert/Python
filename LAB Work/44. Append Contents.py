# Append user input to file

# '\\' means only '\' otherwise error
path = 'D:\MCA\Sem 1\Python\LAB Work\\'

filename = input("Enter filename: ")

# combines path and filename
new = path + filename

with open(new, 'a') as f:
    f.write(input())

f.close()