# Import modules arithmetic & carithmetic

from arithmetic.add import addnos
from arithmetic.sub import subnos
from arithmetic.carithmetic import *

print("Enter two numbers: ")
try :
    a = int(input("Number 1: "))
    b = int(input("Number 2: "))

    print("\n1. Add\n2. Substract\n3. Multiply\n4. Divide")
    c = int(input("\nChoice = "))
    print()

    if c == 1 :
        print("Sum:", addnos(a, b))
    elif c == 2 :
        print("Difference:", subnos(a, b))
    elif c == 3 :
        print("Product:", mul.mulnos(a, b))
    elif c == 4 :
        print("After division:", f"{div.divnos(a, b):.2f}")
except :
    print("Error")