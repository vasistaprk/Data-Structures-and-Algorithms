
def lonelyinteger(a):
    x=a[0]
    for i in range(1,len(a)):
        x=x^a[i]
    
    return(x)


n = int(input().strip())
a = list(map(int, input().rstrip().split()))
result = lonelyinteger(a)
print(result)