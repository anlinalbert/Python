# Copy contents of one file to another

f = open("D:\MCA\Sem 1\Python\LAB Work\myfile.txt",'r')
f1 = open("D:\MCA\Sem 1\Python\LAB Work\output.txt",'w')

for x in f.readlines():
    f1.write(x)
    
f.close()
f1.close()