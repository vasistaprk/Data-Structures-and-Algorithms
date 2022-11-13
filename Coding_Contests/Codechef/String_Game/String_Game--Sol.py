t=int(input())
for i in range(0,t):
    n=int(input())
    s=str(input())
    
    x=int(ord(s[0]))
    for j in range(1,n):
        x=x^int(ord(s[j]))
        
    if(x==0 and n!=1):
        print("YES")
    else:
        print("NO")