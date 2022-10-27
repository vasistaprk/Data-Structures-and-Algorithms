"""Given two numbers X and Y, find the number whose binary representation has X 1's followed by Y 0's.

Input Format

First line of input contains T - number of test cases. Its followed by T lines. 
Each subsequent line contains two integers separated by a space: 
    X - the number of the 1's and Y - the number of 0's which follows the X 1's in the 
    binary representation of the number.

Constraints

10 points
1 <= T <= 100
0 <= X, Y <= 15

40 points
1 <= T <= 105
0 <= X, Y <= 105

Output Format:
For each test case, print the number whose binary representation has X 1's and Y 0's, separated by a new line.
Since this number can be very large, print the result % 1000000007.

Sample Input 0
3
4 3
2 5
10 15

Sample Output 0
120
96
33521664
Explanation 0

Test Case 1:
The binary representation of the number that has 4 ones followed by 3 zeros is 1111000 = 120."""

GT=[0,0,0]
GT[0]=1
GT[1]=2
GT[2]=4
gtfill=2
M=1000000007
for i in range(gtfill+1,1000000):
    s=(((2*GT[i-1]))%M)
    GT.append(s)

import sys
def prin(a):
    sys.stdout.write(str(a)+"\n")


T=int(input())
for i in range(T):
    x,y=[int(i) for i in (input().split())]
    prin ((((GT[x+y]-1)%M-(GT[y]-1)%M)+M)%M)
