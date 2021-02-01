# Reverse a string

def strrev(mystr) :
    if mystr == '' : return ''
    else : return mystr[-1:] + strrev(mystr[0:-1])

mystr = input("Enter a string: ")
print("Reverse:", strrev(mystr))