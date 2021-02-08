# Import listop.py

import listop as l

print("List operations\n1. Remove duplicates\n2. Square list elements")
try :
    c = int(input("Choice = "))

    if c == 1 :
        mylist = input("Enter list elements seperated by commas: ")
        mylist = mylist.split(',')
        print("After removing duplicates:", l.uniqueList(mylist))
    elif c == 2 :
        mylist = input("Enter list elements seperated by commas: ")
        mylist = mylist.split(',')
        print((l.squareList(mylist)))
    else :
        print("Enter a valid choice.")
except :
    print("Error")