"""You are given a maze containing cells. Each cell has certain number of apples. 
You have to start from the top-left position and traverse all the way to the bottom-right position, 
collecting apples on your way. You can move only in right and downward direction,ie, from any cell (i,j) 
you can only move right: (i,j+1) or down: (i+1,j). Find the maximum number of apples you can collect.

Input Format:
First line of input contains T - number of test cases. 
First line of each test case contains N and M - the size of the maze. 
Its followed by N lines, each containing M integers indicating the number of apples in the cell.

Constraints:
1 <= T <= 100
1 <= N,M <= 300
0 <= Aij <= 100

Output Format:
For each test case, print the maximum number of apples you can collect, separated by newline.

Sample Input 0:
2
3 4
1 5 1 4
10 11 0 13
4 15 1 12
4 2
4 5
1 3
10 5
1 0
Sample Output 0:
50
20

Explanation 0

Test Case 1
The path using which you can collect maximum apples is:
Total Apples = 1 + 10 + 11 + 15 + 1 + 12 = 50

Test Case 2
The path using which you can collect maximum apples is:
Total Apples = 4 + 1 + 10 + 5 + 0 = 20"""

import sys

def prin(a):
    sys.stdout.write(str(a)+"\n")
def input():
    return sys.stdin.readline()

def solve(R,C):
    arr = []
    for i in range(0,R):
        a=list(map(int, input().split()))
        arr.append(a)

    for i in range(R-2,-1,-1):
        arr[i][C-1]+=arr[i+1][C-1]

    for i in range(C-2,-1,-1):
        arr[R-1][i]+=arr[R-1][i+1]

    for i in range (R-2,-1,-1):
        for j in range(C-2,-1,-1):
            arr[i][j]+=max(arr[i][j+1],arr[i+1][j])

    return(arr[0][0])


T=int(input())
for i in range(0,T):
    R,C=[int(i) for i in input().split()]
    prin(solve(R,C))
