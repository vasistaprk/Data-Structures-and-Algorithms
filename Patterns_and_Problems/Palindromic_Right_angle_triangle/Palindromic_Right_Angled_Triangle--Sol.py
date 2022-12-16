def solve(n):
    x=64
    for i in range(1,n+1):
        for j in range(1,2*i):
            if(j<=i):
                print(chr(x+j),end=" ")
            else:
                print(chr(x+(2*i)-j),end=" ")
        print()
                

n= int(input())
solve(n)