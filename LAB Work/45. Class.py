# Create Rectangle class with attributes length and breadth and methods to find
# area and perimeter. Compare two Rectangle objects by their area.

class Rectangle :
    def __init__(self):
        self.l = int(input("Enter length of rectangle: "))
        self.w = int(input("Enter breadth of rectangle: "))
    
    def area(self):
        return self.l * self.w

    def perimeter(self):
        return 2 * (self.l + self.w)

r1 = Rectangle()
print('\nArea 1:', r1.area(), '\nPerimeter 1:', r1.perimeter())

print()
r2 = Rectangle()
print('\nArea 2:', r2.area(), '\nPerimeter 2:', r2.perimeter())


if r1.area() == r2.area():
    print('\nRectangles are equal')
else:
    print('\nRectangles are not equal')