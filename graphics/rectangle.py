# Area & perimeter

print("\n**************************")
print("         Rectangle        ")
print("**************************\n")

try :
    l = int(input("Enter rectangle length: "))
    b = int(input("Enter rectangle breadth: "))
    area = l * b
    perimeter = 2  * (l + b)
    print("Area:", "{:.2f}".format(area), "\nPerimeter:", "{:.2f}".format(perimeter))
except :
    print("Error")