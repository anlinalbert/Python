# Remove all odd index characters from string

mystr = "Sophisticated"
mylist = list(mystr)

print("Initial String:", mystr, "\nAfter Removal:", "".join(mylist[1::2]))