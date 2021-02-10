# Find the longest word from a file

longword = ''
c = 0

with open('D:\MCA\Sem 1\Python\Sample Work\input.txt', 'r') as f :
    mylist = f.readlines()
    for word in mylist :
        # to remove '\n' from each word (it adds a extra character creating unexpected output)
        word = word.strip('\n')

        if len(word) > c :
            c = len(word)
            longword = word
    print('Longest word in file:', longword)
f.close()