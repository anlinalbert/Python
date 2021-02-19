# Create a class Rectangle with private attributes length and width. Overload ‘<’
# operator to compare the area of 2 rectangles.

class Rectangle:
    def __init__(self):
        self.__l = int(input("Enter length of rectangle: "))
        self.__w = int(input("Enter breadth of rectangle: "))

    def area(self):
        return self.__l * self.__w

    def __lt__(self, value):
        return (self.__l * self.__w) < (value.__l * value.__w)


r1 = Rectangle()
print('Area 1 =', r1.area())

print()
r2 = Rectangle()
print('Area 2 =', r2.area())

if r1 < r2:
    print('\nRectangle 1 is less than rectangle 2')
else:
    print('\nRectangle 2 is less than rectangle 1')