# Accept a string and return the length of longest word. 
# If the result has more than one word, then print “BINGO”

# reading string
inp_str = input("Enter a string : ")

c = 0
l = 0
w = ""

# checking for longest word
for word in inp_str.split() :
    if len(word) > l :
        l = len(word)
        w = word
    elif len(word) == l :
        c = 1

if c : # if string has words of equal size
    print("BINGO")
else :
    print("Longest word :", w, "\nLength :", l)