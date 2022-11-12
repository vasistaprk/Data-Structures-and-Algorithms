l=int(input())
r=int(input())
max=0

for i in range(l,r+1):
    for j in range(i,r+1):
        if((i^j)>max):
            max=i^j
    
print(max)        
            
"""
Time Complexity of code: O(N^2) where N =l-r
Space Complexity of code: O(1)
"""