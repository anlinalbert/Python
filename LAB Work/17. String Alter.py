# Alter stings

# initial string
str1 = "Walk"

print("Initial string :", str1)

# checking length
l = len(str1)

# altering string
if l >= 2 : 
    if str1[-3:] == "ing" :
        str1 += "ly"
    else :
        str1 += "ing"

print("Altered string :", str1)