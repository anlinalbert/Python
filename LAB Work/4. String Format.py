# Use string formatting

n = int(input("Enter a number : "))
if n < 10 :
    n1 = int(f"{n}")
    n2 = int(f"{n}{n}")
    n3 = int(f"{n}{n}{n}")
    print(f"Sum of {n} + {n}{n} + {n}{n}{n} =", n1 + n2 +n3)
else :
    print("Enter a number lesser than 10")
