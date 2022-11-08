#Taking Input from user.
t=int(input()) #test cases

for l in range(0,t):
    n=int(input()) #Sqaure matrix Size
    #Intialization of matrix
    a=[[0 for i in range(0,n)]for j in range(0,n)]
    for i in range(0,n):
            a[i]=list(map(int, input().split())) #Storing input from user in list.
    #OUTPUT:
    result=[0]*((n*2)-1)
    for i in range(0,n):
        for j in range(0,n):
            result[(i-j)+(n-1)]+=a[i][j]
    
    for i in range(0,(n*2)-1):
        print(result[i],end=" ")
    
    print()