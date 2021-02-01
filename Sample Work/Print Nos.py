# Write a program that print numbers from 1 to 20. For every multiple of 3,
# print ‘Fizz’, for every multiple of 5, print ‘Buzz’ and for every multiple of
# both 3 and 5 print ‘FizzBuzz’, instead of the original number.

for i in range(1, 20 + 1) :
    if not i % 3 and not i % 5 :
        print("FizzBuzz")
    elif not i % 3 :
        print("Fizz")
    elif not i % 5 :
        print("Buzz")
    else :
        print(i)