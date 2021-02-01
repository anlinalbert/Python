# Area & perimeter

import math

print("\n**************************")
print("            Sphere          ")
print("**************************\n")

try :
    r = int(input("Enter radius of sphere: "))
    area = 4 / 3  * math.pi * r * r * r
    perimeter = 4 * math.pi * r * r
    print("Volume:", "{:.2f}".format(area), "\nSurface:", "{:.2f}".format(perimeter))
except :
    print("Error")