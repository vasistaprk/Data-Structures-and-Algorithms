"""
Given an array of N integers in which every element repeat twice except one. 
Find the element which is not repeating.

"""
def bruteforce(arr,n):
    for i in range(0,n): #O(N)
        count=0;
        x=arr[i];
        for j in range(0,n): #O(N)
            if(arr[j]==x):
                count+=1
        if(count==1):
            return x

"""
Time Complexity: O(N^2)
Space Complexity: O(1)
"""

def solve(arr,n):
    ans=arr[0]
    for i in range(1,n):
        ans=ans^arr[i]
    return(ans)


n=int(input())
arr=list(map(int,input().split()))
print(bruteforce(arr,n))
print(solve(arr,n))

"""
Time Complexity: O(N)
Space Complexity: O(1)
"""