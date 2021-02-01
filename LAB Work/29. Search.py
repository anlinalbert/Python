# Search and find no.of occurences

mylist = [1, 2, 25, 2, 1, 2, 75, 2]
c = 0
i = 0
key = 2

while i < len(mylist) :
    if mylist[i] == key :
        c = c + 1 
    i = i + 1

print("My list:", mylist, "\nKey:", key)
if c :
    print("Number of occurences:", c)
else :
    print("Item not found")