##row=int(input('Enter the no of rows'))
##cols=int(input('Enter the no of cols'))
##a=65
##for i in range(row):
##    for j in range(cols):
##        print(chr(a),end=" ")
##        a+=1 
##    print()
##
##row=int(input('Enter the no of rows'))
##for i in range(row+64,64,-1 ):
##    for j in range(65,i+1):
##        print(chr(j),end=" ") 
##    print()
## 

##row=int(input('Enter the no of rows'))
##for i in range(row+64,64,-1 ):
##    for j in range(65,i+1):
##        print(chr(i),end=" ") 
##    print()
## 

row=int(input('enter the rows'))
for i in range(row):
    for j in range(row-i):
        print(" ",end="")
    for k in range(i+1):
        print("*",end=" ")
    print("")
