def digits(n):
    ans=0
    while(n>0):
        ans+=1
        n=n//10
    return ans

def armstrong(n,digits):
    sum=0
    x=n
    while(n>0):
        sum=sum+((n%10)**digits)    
        n=n//10
    if(sum==x):
        print("YES")
    else:
        print("NO")


n=int(input())
digits=digits(n)
armstrong(n,digits)