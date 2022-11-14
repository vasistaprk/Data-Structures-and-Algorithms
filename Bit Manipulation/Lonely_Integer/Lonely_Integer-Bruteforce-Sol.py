
def lonelyinteger(a):

    for i in range(0,len(a)):
        x=a[i]
        count=0
        for j in range(0,len(a)):
            if(x^a[j]==0 ):
                count+=1
        if(count==1):
            return(x)
            

n = int(input().strip())
a = list(map(int, input().rstrip().split()))
result = lonelyinteger(a)
print(result)

"""
This has Time complexity of O(N^2)
This has Space complexity of O(1)
"""
  