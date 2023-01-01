def solve(s):
    x=len(s)
    max=0
    for i in range(0,len(s)-1):
        prefix=s[ :i+1]
        suffix=s[-(i+1): ]
        if(prefix==suffix and len(prefix)>max):
            max=len(prefix)
                
    return(max)
        
s=input()
print(solve(s))

"""
Time Complexity: O(N)
Space Complexity: O(1)
"""