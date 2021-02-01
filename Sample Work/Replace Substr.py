# Replace substring

mystr = "this is not very very bad for sure"

print("Initial string :", mystr)

pos1 = mystr.find("not")
pos2 = mystr.find("bad")

if pos1 < pos2 :
    mystr = mystr[:pos1] + "good" + mystr[pos2 + 3:]
    mystr = mystr.replace("bad not", "good")
    print("Final string :", mystr)