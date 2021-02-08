# Imported by List Ops.py

# removes duplicate items in list
def uniqueList(l) :
    l = set(l)
    return list(l)

def squareList(l) :
    # to convert list items to integers
    tointeger  = [int(j) for j in l]

    # squaring
    return [i ** 2 for i in tointeger]