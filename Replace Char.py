# Replace first string character

s = input("Enter a string : ")
new_s = s[0]
s = s.replace(new_s, '&')
s = new_s + s[1:]
print("New string :", s)