# ZeroDivisionError and ValueError

try :
    n = int(input("Enter a number: "))
    r = 5 / n
except ZeroDivisionError as Z :
    print("Error :", Z)
except ValueError as V :
    print("Error :", V)