# Area & perimeter

print("\n**************************")
print("           Cuboid           ")
print("**************************\n")

try :
    l = int(input("Enter cuboid length: "))
    w = int(input("Enter cuboid width: "))
    h = int(input("Enter cuboid height: "))
    area = l * w * h
    perimeter = 2 * (l*w + l*h + w*h)
    print("Volume:", "{:.2f}".format(area), "\nSurface:", "{:.2f}".format(perimeter))
except :
    print("Error")