# Delete comments from a file

with open("D:\MCA\Sem 1\Python\Sample Work\input.txt", "r") as f:
    # reading file into list
    text = f.readlines()
f.close()

with open("D:\MCA\Sem 1\Python\Sample Work\input.txt", "w") as f:
    for word in text:
        if not word.startswith('#'):
            f.write(word)
f.close()
