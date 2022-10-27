"""All containers in the world are divided into two categories - with or without trotyl (TNT). 
Only a fool would put a box with TNT on another box with TNT. Since you are not a fool (hmm ...), 
you know exactly that TNT explode, especially if it is on another box with TNT. 
You are in the room in which there are two types of boxes in a huge quantity. 
Suddenly, the lifter comes into the room from the hatch. It fails. 
It is intended to build a tower with n boxes. 
In order to estimate your chance to survive, you have to count the number of outcomes where nothing explodes.

By the way, what a reasonable person like you doing in a room with a bunch of TNT?

Input
One integer n (1 ≤ n < 45).

Output
Print the number of good outcomes."""

GT=[0,0]
GT[0]=1
GT[1]=2
gtfill=1

def solve(n):
    if(n<=1):
        return (GT[n])
    
    global gtfill
    if( gtfill >= n):
        return(GT[n])
    
    for i in range(gtfill+1,n+1):
        GT.append(GT[i-1]+GT[i-2])
        gtfill+=1
    
    return(GT[n])



n=int(input())
print(solve(n))