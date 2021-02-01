# Count vowels

c = 0

mystr = input("Enter a sentence: ")

for i in mystr:
    if (i in 'aeiouAEIOU') :
        c = c + 1

print("Number of vowels:", c)