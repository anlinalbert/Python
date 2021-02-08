# Imported by String Ops.py

# reverse string
def stringRev(s) :
    print("String reverse :", s[::-1])

# count upper & lower cases
def countUpperAndLowerCase(sentence):
    upper = 0
    lower = 0
    for i in sentence:
        if i >='A' and i <= 'Z':
            upper += 1
        elif i >= 'a' and i <= 'z':
            lower += 1
    print("Upper case: " + str(upper))
    print("Lower case: " + str(lower))

# check whether palindrome
def isPalindrome(s):
    rev = s.casefold()
    rev = rev[::-1]
    if s.lower() == rev :
        print("Palindrome")
    else:
        print("Not palindrome")

# check whether pangram
def isPangram(s): 
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    c = True
    for char in alphabet: 
        if char not in s.lower(): 
            c = False
    if c :
        print("Pangram")
    else :
        print("Not pangram")