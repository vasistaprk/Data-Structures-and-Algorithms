"""Given a standard 6-sided dice, find the number of ways to get a sum of N.

Input Format

First line of input contains T - number of test cases. 
Its followed by T lines, each line contains N - the desired sum.

Constraints

1 <= T <= 100000
1 <= N <= 100000

Output Format

For each test case, print the number of ways to get a sum of N, separated by newline. 
Since the answer can be very large, print answer % 1e9+7.

Sample Input 0

5
3
11
7
5
500
Sample Output 0

4
976
63
16
765996555
Explanation 0

Test Case 1
You can get a sum of 3 in the ways:
(1,1,1), (1,2), (2,1), (3)"""

GT=[0,0,0,0,0,0]
GT[0]=1
GT[1]=1
GT[2]=2
GT[3]=4
GT[4]=8
GT[5]=16
gtfill=5


def solve(n):
    if(n<=5):
        return (GT[n])
    
    global gtfill
    if( gtfill >= n):
        return(GT[n])
    
    for i in range(gtfill+1,n+1):
        ans=0
        for j in range(1,7):
            ans=(ans%M+(GT[i-j])%M)%M

        GT.append(ans)
        gtfill+=1

    
    return(GT[n])



M=1000000007
T=int(input())
for i in range(0,T):
    n=int(input())
    print(solve(n))