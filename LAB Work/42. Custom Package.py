# Custom package

from graphics.circle import apcircle
from graphics.rectangle import aprectangle
from graphics.dgraphics import *

print("Area & Perimeter\n\n1. Circle\n2. Rectangle\n3. Cuboid\n4. Sphere\n")

try :
    c = int(input("Choice = "))
    print()
    if c == 1 :
        r = int(input("Enter radius of circle: "))
        apcircle(r)
    elif c == 2 :
        l = int(input("Enter rectangle length: "))
        b = int(input("Enter rectangle breadth: "))
        aprectangle(l, b)
    elif c == 3 :
        l = int(input("Enter cuboid length: "))
        w = int(input("Enter cuboid width: "))
        h = int(input("Enter cuboid height: "))
        cuboid.apcuboid(l, w, h)
    elif c == 4 :
        r = int(input("Enter radius of sphere: "))
        sphere.apsphere(r)
except :
    print("Error")