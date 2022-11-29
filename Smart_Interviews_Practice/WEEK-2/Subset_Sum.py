"""
Given an array of integers "Arr" and sum "K". 
To check whether there exists a subset in Arr which sum upto k.

No.of subsets for given set of N elements will be 2^N.
"""
def checkbit(i,j):
    return((i>>j)&1)

def bit_manipulation_method(arr,n,k):
    for i in range(0,(1<<n)): #O(2^N)
        sub=0
        for j in range(0,n): #O(N)
            if(checkbit(i,j)==1): 
                #If j-th bit of i is 1, then we consider j-th(index) number of array. 
                sub=sub+arr[j]
        if(sub==k):
            return True

    return False

arr=list(map(int,input().split()))
n=len(arr)
k=int(input())
print(bit_manipulation_method(arr,n,k))

"""
Time Complexity: O(2^N x N)
Space Complexity: O(1)
"""