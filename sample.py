f = open("E:\\welcome1.txt", 'w')
str1=input("enter Y/y if you want to write some text in it other enter N/n\n")
if(str1=="Y" or str1=="y"):
    str2=input("enter text you want to write into the fil\n")
    f.write(str2)
    f.close()
f = open("E:\\welcome1.txt", 'r')
print(f.read()) 
