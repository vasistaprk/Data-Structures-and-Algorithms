def solve(n):
    for i in range(1,n+1):
        for j in range(1,n*2):
            if(j>n-i and j<n+i):
                print("*",end="")
            else:
                print(" ",end="")
        print()
    return
            

n=int(input())
solve(n)
