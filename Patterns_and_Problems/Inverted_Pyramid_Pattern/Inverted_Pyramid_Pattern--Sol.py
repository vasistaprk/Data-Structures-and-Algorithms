def solve(n):
    for i in range(1,n+1):
        for j in range(1,n+1):
            if(i==1 or j==1):
                print("*",end=" ")
            elif(i>1 and j==(n-i+1)):
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print()
    return
                
    
n=int(input())
solve(n)