# Sum of first N whole numbers

def sumN(n) :
    if not n : return 0
    if n == 1 : return 1
    else : return n + sumN(n - 1)

n = int(input("Enter a limit: "))
print("Sum of N whole numbers:", sumN(n))