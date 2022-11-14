class Solution:
    # @param A : unsigned integer
    # @return an unsigned integer
    def reverse(self, A):
        result=0
        for i in range(0,32):
            if(A&1==1):
                result=result+(2**(32-i-1))
            A=A>>1
        return result 