n=int(input())
for i in range(0,(n*2)-1):
    for j in range(0,n):
        if(i<n and j<=i):
            print("*",end="")
        elif(i>=n and j<=((2*n)-2-i)):
            print("*",end="")
        else:
            print(" ",end="")
    print()
    