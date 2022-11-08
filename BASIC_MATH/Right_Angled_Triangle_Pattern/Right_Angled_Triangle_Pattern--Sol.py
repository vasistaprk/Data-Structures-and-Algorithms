#Taking Input from user.
t=int(input()) #test cases

for i in range(0,t):
    x=int(input()) #User Input

    #OUTPUT:
    print("Case #"+str((i+1))+":")
    for i in range(0,x):
        for j in range(0,x):
            if((i+j)<x-1):
                print(" ",end="")
            else:
                print("*",end="")
                
        print("")