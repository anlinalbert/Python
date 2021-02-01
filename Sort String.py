# Sort string case insensitively

mylist_unsorted = ["Anlin", "abdul", "alice", "Alexander"]

# to sort list case insensitively
mylist_sorted = sorted(mylist_unsorted, key = str.casefold)

# printing
print("Unsorted list :", mylist_unsorted, "\nSorted list :", mylist_sorted)