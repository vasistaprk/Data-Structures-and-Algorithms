class Solution:
    def solve(self, A):
        count=0;
        while(A!=0):
            if(A&1==0):
                count+=1
                A=A>>1
            else:
                break
        
        return count 