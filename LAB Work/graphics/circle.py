# Area & perimeter

def apcircle(r) :
    import math

    try :
        area = math.pi * r * r
        perimeter = 2  * math.pi * r
        print("Area:", "{:.2f}".format(area), "\nPerimeter:", "{:.2f}".format(perimeter))
    except :
        print("Error")