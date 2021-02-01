# ValueError

try :
    n = int(input("Enter a number: "))
    if n > 90 and n < 120 : 
        pass
    else :
        raise ValueError("Abnormal Condition")
except ValueError as v :
    print(v)
