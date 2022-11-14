class Solution:
    def numSetBits(self, A):
        count=0
        while(A!=0):
            count+=1
            A=A&(A-1)
        
        return count