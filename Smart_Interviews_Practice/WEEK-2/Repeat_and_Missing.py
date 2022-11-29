"""
Given an array of numbers(sequnce of number) in which one element is repeating and 
other is missing from given series.
Example: arr= 5 2 8 1 6 1 4 3
Repeated element: 1
Missing element: 7

1 <= ar[i] <= N(8)
"""
def checkbit(N,i):
    return((N>>i)&1)

def bit_manipulation_method(arr,n):
    x=0
    for i in range(0,n):
        x=x^arr[i]^(i+1)
    # We get x=Rem^Miss
    for i in range(0,32):
        if(checkbit(x,i)==1):
            b=i
            break
    A=B=0
    """
    We make two grps of numbers, 
    A: will have all numbers having i-th bit as 1
    B: will have all numbers having i-th bit as 1
    """
    for i in range(0,n):
        if(checkbit(arr[i],b)==0):
            B=B^arr[i]
        else:
            A=A^arr[i]
        t=i+1
        if(checkbit(t,b)==0):
            B=B^t
        else:
            A=A^t
        
    if(A in arr):
        Rem=A
        Miss=B
    else:
        Rem=B
        Miss=A
    
    return (Rem,Miss)

arr=list(map(int,input().split()))
n=len(arr)
print(bit_manipulation_method(arr,n))

"""
Time Complexity: O(N)
Space Complexity: O(1)
"""