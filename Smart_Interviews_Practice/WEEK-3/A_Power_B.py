"""
Recursive method to fine A^B.
Given A and B, find the A^B and use %M if given.
"""
#M=1e9+7
def recursive_method(a,b):
    x=recursive_method(a,b/2)
    if(b&1 == 0):
        return x*x
    return a*x*x

a,b = map(int,input().split())
print(recursive_method(a,b))

"""
Time Complexity: O(Log(b))
Space Complexity: O(1)
"""