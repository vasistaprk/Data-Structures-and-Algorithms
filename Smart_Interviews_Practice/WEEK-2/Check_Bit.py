"""
Given a Number N and find whether a i(th) bit of Binary representation of N is Set bit(1) or not.

N=10 
Binary: ... 0000 1010
set bits are 2nd and 4th bit from right.
Checkbit(5,4)=True
Checkbit(5,3)=False

Constraints:
0 <= i <= 30
o <= n <= 10^9
"""
def Checkbit(N,i):
    return ((N>>i)&1)

N=int(input("Enter a Number: "))
i=int(input("Enter bit Number to check: "))
print(Checkbit(N,i))

"""
Case 1: return ((N>>i)&1)
Case 2: return (N>>i)%2 
Case 3: return (N&(1<<i))

Case 1 and 2 are same on bitlevel operations.
Case 3: if result = 0 then i(th) bit is 0 else result would be 2^i instead of just 1 unlike in previous case.
"""