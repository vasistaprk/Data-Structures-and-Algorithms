x=int(input())
ar =list(map(int, input().split()))

for i in range(0,x):
    l=ar[i]
    count=0
    for j in range(i,x):
        if(ar[j]==l and ar[j]!=-1):
            count=count+1
            ar[j]=-1
            
    if(count==1):
        print(l,end=" ")

"""
//Time Complexity: O(N^2)
//Space CVomplexity: O(1)
"""