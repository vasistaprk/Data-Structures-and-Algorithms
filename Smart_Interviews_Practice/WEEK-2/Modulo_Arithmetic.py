"""
M = 1e9+7 in most of the cases. (M=1000000007)
MODULO ARITHMETIC:
(a+b)%M = (a%M + b%M) %M
(a*b)%M = (a%M * b%M) %M  (Multiplication is repeated is addition)
(a-b)%M = (a%M - b%M +M) %M (We must also cover up negatice results.)
(a/b)%M = (a*(1/b)) %M = (a%M * (b^-1)%M) %M
    In this Case we use Inverse Modulo.
    Extended Euclids Algorithm.

Considering A^N alogorithm.
"""
def solve(a,n):
    M=1e9+7
    ans=1
    a=a%M
    for i in range(0,n):
        """
        1. ans %M = (ans%M * a%M)%M
        we must decrease % operations as many as possible as they are costly and are heavy for the system.
        we can remove ans%M as for every iteration the previous iteration have already given us ans%M only.
        2. ans = (ans * a%M)%M
        we can even exclude a%M at every iteration by doing it once at beginning.
        """
        ans=(ans * a)%M

    return ans

a,n=map(int,input().split())
print(solve(a,n))