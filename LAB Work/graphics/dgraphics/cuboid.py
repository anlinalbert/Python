# Area & perimeter

def apcuboid(l, w, h) :
    try :
        area = l * w * h
        perimeter = 2 * (l*w + l*h + w*h)
        print("Volume:", "{:.2f}".format(area), "\nSurface:", "{:.2f}".format(perimeter))
    except :
        print("Error")