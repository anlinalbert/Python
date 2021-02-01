# Write a program that accepts a comma separated sequence of
# words as input and print unique words in sorted order.

word = input("Enter words seperated by commas: ").split(',')

myset = set(word)
mylist = list(myset)

sortedlist = sorted(mylist, key = str.casefold)

print(sortedlist)