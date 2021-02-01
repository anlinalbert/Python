# Nth Fibo

def fibo(n) :
    if not n : return 0
    if n == 1 : return 1
    else : return fibo(n-1) + fibo(n-2)

n = int(input("Enter a number: "))
print("Nth fibo:", fibo(n))