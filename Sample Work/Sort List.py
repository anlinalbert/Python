# Sort number list in ascending & decending

usr_inp = input("Enter a list of numbers : ")
mylist = usr_inp.split(',')

# printing
print("\nList :", mylist)

# to sort list
mylist.sort()

# printing
print("In Ascending :", mylist)

# to sort list
mylist_dec = mylist.sort(reverse = True)

# printing
print("In Decending :", mylist)