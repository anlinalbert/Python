# Print even nos from list

mylist = [1, 342, 231, 35, 4, 245, 237, 4, 2]
i = 0

print("My list:", mylist, "\nEven Numbers:")
while i < len(mylist) :
    if mylist[i] == 237 :
        break
    if not mylist[i] % 2 :
        print(mylist[i])
    i = i + 1