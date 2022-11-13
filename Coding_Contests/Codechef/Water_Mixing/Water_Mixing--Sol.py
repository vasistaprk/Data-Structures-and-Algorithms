# cook your dish here
t=int(input())
for i in range(0,t):
    a,b,x,y=map(int,input().split())
    
    if(a==b):
        print("YES")
    elif(a>b):
        if(a-b<=y):
            print("YES")
        else:
            print("NO")
    else:
        if(b-a<=x):
            print("YES")
        else:
            print("NO")
        