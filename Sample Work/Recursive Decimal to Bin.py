# Decimal to binary

def binary(n) :
    if not n : return 0
    elif n >= 1 : 
        binary(n // 2)
        print(n % 2, end = '')

n = int(input("Enter a decimal number: "))
print("Binary number:")
binary(n)