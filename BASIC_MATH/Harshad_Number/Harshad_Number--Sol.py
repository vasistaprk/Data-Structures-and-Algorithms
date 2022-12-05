def harshad(n):
    sum=0
    x=n
    while(n>0):
        sum=sum+(n%10)
        n=n//10
    if(x%sum==0):
        print("Yes")
    else:
        print("No")    


n=int(input())
harshad(n)