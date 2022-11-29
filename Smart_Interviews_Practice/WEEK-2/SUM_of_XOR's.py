"""
Given an array Arr = a b c
SUM of XOR's will be:
=> 0+(a^a)+(a^b)+(a^c)+(b^a)+(b^b)+(b^c)+(c^a)+(c^b)+(c^c)
=> 0+2[(a^b)+(a^c)+(b^c)]

if Arr = a b c d
SUM of XOR's will be:
=> 0+2[(a^b)+(a^c)+(a^d)+(b^c)+(b^d)+(c^d)]
"""
def solve1(arr,n):
    ans=0
    for i in range(0,n):
        for j in range(i+1,n):
            ans=ans+(arr[i]^arr[j])
    
    return(ans*2)

"""
Time Complexity: O(N^2)
Space Complexity: O(1)
"""
def checkbit(N,i):
    return((N>>i)&1)

def solve2(arr,n):
    ans=0
    for i in range(0,31):
        count_i_0=0
        count_i_1=0
        for j in range(0,n):
            if(checkbit(arr[j],i)==1):
                count_i_1+=1
            else:
                count_i_0+=1
        ans=ans+((count_i_0*count_i_1)+(1<<i))

    return(ans)

"""
Time Complexity: O(N)
Space Complexity: O(1)
"""

arr=list(map(int,input().split()))
n=len(arr)
print(solve1(arr,n))
print(solve2(arr,n))