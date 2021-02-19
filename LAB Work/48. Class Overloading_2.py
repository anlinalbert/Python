# Create a class Time with private attributes hour, minute and second. Overload
# ‘+’ operator to find sum of 2 time.

class Time:
    def __init__(self):
        self.__hour = int(input('Enter hour: '))
        self.__minute = int(input('Enter minute: '))
        self.__second = int(input('Enter second: '))

    def __add__(self, value):
        return self.__hour + value.__hour, self.__minute + value.__minute, self.__second + value.__second

print('Time 1:')
t1 = Time()

print('\nTime 2:')
t2 = Time()

# to get all values from return
h, m, s = t1 + t2

print('\nSum of time 1 & 2 =', h, 'hour :', m, 'minute :', s, 'second')