# Area & perimeter

def aprectangle(l, b) :
    try :
        area = l * b
        perimeter = 2  * (l + b)
        print("Area:", "{:.2f}".format(area), "\nPerimeter:", "{:.2f}".format(perimeter))
    except :
        print("Error")