"""Find of number of binary strings of length N, such that there are no adjacent 1s in that string.

Input Format

First line of input contains T - number of test cases. Its followed by T lines, each line contains 
N - length of the binary string.

Constraints

1 <= T <= 100000
1 <= N <= 100000

Output Format

For each test case, print the number of binary strings of length N, separated by newline. 
Since the answer can be very large, print answer % 1e9+7.

Sample Input 0

5
3
11
7
5
500
Sample Output 0

5
233
34
13
73724597
Explanation 0

Test Case 1
You can construct the following binary strings of length 3 with no adjacent 1s:
000, 001, 010, 100, 101"""

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
        GT.append((GT[i-1]%M+GT[i-2]%M)%M)
        gtfill+=1
    
    return(GT[n])



M=1000000007
T=int(input())
for i in range(0,T):
    n=int(input())
    print(solve(n))