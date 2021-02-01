# Word frequency in a sentence

count = {}
mystr = "India is my country I love my country"
for i in mystr.split():
    count[i] = count.get(i,0) + 1
print("Initial String :", mystr, "\nWord count :", count)