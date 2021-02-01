# Remove nth character

s = input("Enter a string : ")
pos = int(input("Enter position of character to be removed : "))
print(s[:pos-1] + s[pos:])