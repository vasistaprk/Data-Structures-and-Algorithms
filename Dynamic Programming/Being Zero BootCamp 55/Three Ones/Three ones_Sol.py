"""Find the number of sequences of length n, consisting only of zeros and ones, that do not have three 
one's in a row.

Input
The length of the sequences n (1 ≤ n ≤ 105).

Output
Print the required number of sequences modulo 12345.
"""


GT=[0,0,0]
GT[0]=1
GT[1]=2
GT[2]=4
gtfill=2

def solve(n):
    if(n<=2):
        return (GT[n])
    
    global gtfill
    if( gtfill >= n):
        return(GT[n])
    
    for i in range(gtfill+1,n+1):
        GT.append(((GT[i-1]%M+GT[i-2]%M)%M+GT[i-3]%M)%M)
        gtfill+=1
    
    return(GT[n])



M=12345

n=int(input())
if(n<0):
    print(1)
else: 
    print(solve(n))