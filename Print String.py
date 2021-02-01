# Accept a string and an integer, n, from the user.
# (a) Print first 2 characters of the string ‘n’ times, if length of string is
# greater than or equal to 5
# (b) Print n copies of input string, if length of string is less than 5

mystr = input("Enter a string: ")
n = int(input("Enter a number: "))

for i in range(n) :
    if (len(mystr) >= 5) :
        print(mystr[0:2])
    elif (len(mystr) < 5) :
        print(mystr)