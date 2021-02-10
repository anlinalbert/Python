# Capitalize each word in a file

def capitalize():
    for i in f:
        cap = i.title()
        print(cap)


f = open('D:\MCA\Sem 1\Python\Sample Work\input.txt', 'r')
capitalize()
f.close()
