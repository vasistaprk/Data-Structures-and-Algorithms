"""
Given a and n, compute a^n with Modulo M if given.
Easy to keep is to use power array.

"""
#M=1e9+7
def bit_manipulation_method(a,n):
    x=a #x=a%M
    ans=0
    while(n!=0):
        if((n&1)==1): 
            """
            If we observe we get TC as log(N).
            For 4<N<=8 : log(N) = 3
            For 8<N<=16 : log(N) = 4
            For 16<N<=32 : log(N) = 5
            """
            ans=ans+x #ans = (ans%M)+x
        x=x*x
        n=n>>1

    return ans

a,n=map(int,input().split())
print(bit_manipulation_method(a,n))

"""
Time Complexity: O(Log(N))
Space Complexity: O(1)
"""