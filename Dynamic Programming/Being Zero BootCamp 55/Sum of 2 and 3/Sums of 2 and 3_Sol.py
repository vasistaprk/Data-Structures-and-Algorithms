"""Changu and Mangu are brothers. Changu likes 2 and Mangu likes 3. 
They decided to express each number as sum of 2 and 3.

They need your help. They want you to tell them the number of ways of writing a number as ordered 
sums of 2 and/or 3.

For example,  there are 4 ways to write 8 as an ordered sum of 2s and/or 3s:

 2 + 2 + 2 + 2

 2 + 3 + 3

3 + 2 + 3

3 + 3 + 2

Input
The first line contains T, the number of test cases. It is followed by T lines, each containg a number N.

Output
You have to print the number of ways of writing N as ordered sum of 2 and/or 3. 
You have to print the answer mod 1000000007.

Example
Input:

3
2
3
8

Output:

1
1
4

Constraints:

T<=100000

1<=N<=1000000"""

import sys
def prin(a):
    sys.stdout.write(str(a)+'\n')
def input():
    return sys.stdin.readline()

GT=[0,0,0]
GT[0]=1
GT[1]=0
GT[2]=1
gtfill=2

def solve(n):
    if(n<=2):
        return (GT[n])
    
    global gtfill
    if( gtfill >= n):
        return(GT[n])
    
    for i in range(gtfill+1,n+1):
        GT.append((GT[i-2]%M+GT[i-3]%M)%M)
        gtfill+=1
    
    return(GT[n])



M=1000000007
T=int(input())
for i in range(0,T):
    n=int(input())
    print(solve(n))