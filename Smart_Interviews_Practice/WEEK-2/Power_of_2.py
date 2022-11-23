""""
Check whether a given number is a Power of two or not.
--> If the given number is power of 2, then the binary representation of thar number 
    has only one set bit.
"""

def setbits(N):
    count=0
    while(N!=0):
        count+=1
        N=(N&(N-1))
    return count

N=int(input())
if(setbits(N)==1):
    print("YES")
else:
    print("NO")
