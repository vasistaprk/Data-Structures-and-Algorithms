import math
"""
For a given N find the number.of Divisors it has.
"""
def solve1(n):
    count=2
    for i in range(2,(n/2)+1): #-->O(N/2)
        if(n%i==0):
            count+=1
    return count

"""
Time Complexity = O(N)
Space Complexity = O(1)
"""

def solve2(n):
    count=2
    for i in range(2,int(math.sqrt(n)+1)):
        if (n%i==0):
            count+=2 #i and N/i
    return count

"""
Time Complexity = O(root(N))
Space Complexity = O(1)
"""

n=int(input())
print(solve1(n))
print(solve2(n))