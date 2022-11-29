"""
Given an array Arr = a b c
XOR of Sum's will be: 
=> 0^(a+a)^(a+b)^(a+c)^(b+a)^(b+b)^(b+c)^(c+a)^(c+b)^(c+c)
=> 0^(a+a)^(b+b)^(c+c)
"""
def solve1(arr,n):
    ans=0
    for i in range(0,n):
        for j in range(0,n):
            ans=ans^(arr[i]+arr[j])
    
    return(ans)

"""
Time Complexity: O(N^2)
Space Complexity: O(1)
"""

def solve2(arr,n):
    ans =0 
    for i in range(0,n):
        ans=ans^(2*arr[i])
    return ans

"""
Time Complexity: O(N)
Space Complexity: O(1)
"""

arr=list(map(int,input().split()))
n=len(arr)
print(solve1(arr,n))
print(solve2(arr,n))