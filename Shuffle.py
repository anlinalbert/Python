# Shuffle user input

import random

usr_inp = input("Enter a list : ")
mylist = usr_inp.split(',')

# shuffle
random.shuffle(mylist)

#printing
print("Shuffled list :", mylist)