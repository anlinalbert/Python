# Write a program to delete sentences from a file having a specific word
# entered by the user.

try :
    user_input =  input('Enter a word: ')
    
    with open('D:\MCA\Sem 1\Python\Sample Work\input.txt', 'r') as f :
        mylist = f.readlines()
        for word in mylist :
            if user_input not in word :
                print(word)
except :
    print('Error')

finally :
    f.close()