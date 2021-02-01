# Area & perimeter

import math

print("\n**************************")
print("          Circle          ")
print("**************************\n")

try :
    r = int(input("Enter circle radius: "))
    area = math.pi * r * r
    perimeter = 2  * math.pi * r
    print("Area:", "{:.2f}".format(area), "\nPerimeter:", "{:.2f}".format(perimeter))
except :
    print("Error")