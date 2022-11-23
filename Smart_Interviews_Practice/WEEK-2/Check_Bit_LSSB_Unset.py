"""
N & (N-1) --> Unsets the least significant Set bits.

"""
def setbits(N):
    count = 0
    while(N>0 or N!=0):
        count+=1
        N=(N&(N-1))#This statement slowly changes all set bits to 0.
    return count

N=int(input())
print(setbits(N))

"""
APLLICATIONS:

1. Check if a given number is power of 2 or not.
    ---> If a given number is power of two then it has only one set bit.
    ---> In above code count=1.
"""



