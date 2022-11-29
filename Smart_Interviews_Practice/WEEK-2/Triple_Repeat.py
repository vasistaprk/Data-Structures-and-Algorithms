"""
Given a Array in which every number repeats thrice except one, find the unique element.
We construct the unique number bit by bit.
"""
def checkbit(N,i):
    return((N>>i)&1)

def bit_manipulation_method(arr,n):
    result=0
    for i in range(0,31): #for 32 bit integer --> O(32)
        Count_i_1=0 # Count of numbers having i-th bit as 1
        for j in range(0,n): #O(N)
            if(checkbit(arr[j],i)==1):
                Count_i_1+=1
        if(Count_i_1%3!=0):
            result+=(1<<i)

    return(result)

arr=list(map(int,input().split()))
n=len(arr)
print(bit_manipulation_method(arr,n))

"""
Time Complexity: O(32N)-->O(N)
Space Complexity: O(1)
"""
