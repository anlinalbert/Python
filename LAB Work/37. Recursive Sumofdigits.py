# Sum of digits

def sumdigits(n) :
    if not n : return 0
    if n == 1 : return 1
    else : return int(n % 10) + sumdigits(n / 10)

n = int(input("Enter a number: "))
print("Sum of digits:", sumdigits(n))