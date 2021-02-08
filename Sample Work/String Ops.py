# Import stringop.py

import stringop as s

print("String Operations\n1. Reverse String\n2. Count lower and upper cases\n3. Check whether palindrome\n4. Check whether pangram")
try :
    c = int(input("\nChoice = "))
    print()

    if c == 1 :
        mystring = input("Enter the string to be reversed: ")
        s.stringRev(mystring)
    elif c == 2 :
        mystring = input("Enter a string: ")
        s.countUpperAndLowerCase(mystring)
    elif c == 3 :
        mystring = input("Enter a string: ")
        s.isPalindrome(mystring)
    elif c == 4 :
        mystring = input("Enter a string: ")
        s.isPangram(mystring)
    else :
        print("Enter a valid choice.")
except :
    print("Error")