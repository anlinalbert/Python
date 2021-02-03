# Area & perimeter

def apsphere(r) :
    import math

    try :
        area = 4 / 3  * math.pi * r * r * r
        perimeter = 4 * math.pi * r * r
        print("Volume:", "{:.2f}".format(area), "\nSurface:", "{:.2f}".format(perimeter))
    except :
        print("Error")