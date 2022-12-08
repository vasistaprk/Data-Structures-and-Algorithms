w,l=map(int,input().split())
for i in range(0,l):
    for j in range(0,w):
        if(i==0 or i==l-1):
            print("*",end="")
        elif(j==0 or j==w-1):
            print("*",end="")
        else:
            print(" ",end="")
    print()