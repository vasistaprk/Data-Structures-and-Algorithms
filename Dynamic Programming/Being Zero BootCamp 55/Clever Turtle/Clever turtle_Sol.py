"""There is a field of cellular size m × n. The turtle sits in the lower left corner. 
It can go only right or up. Before getting to the top right corner, it is interested in the question: 
how many ways are there to get from the origin to the upper right corner?

Although the turtle is clever, it can't count so much. Help the turtle to find an answer to your question.

Input
Two positive integers m and n not exceeding 30.

Output
Print the number of ways to get from the lower left corner to the upper right one."""

import sys

def prin(a):
    sys.stdout.write(str(a)+'\n')
def input():
    return sys.stdin.readline()

def solve(m,n):
    arr = [[0 for i in range(n)] for j in range(m)]

    for i in range(m-1,-1,-1):
        arr[i][n-1]=1
    for j in range(n-1,-1,-1):
        arr[m-1][j]=1

    for i in range (m-2,-1,-1):
        for j in range(n-2,-1,-1):
            if(arr[i][j]==-1):
                arr[i][j]=0
            else:
                arr[i][j]=(arr[i][j+1]+arr[i+1][j])

    return(arr[0][0])

m,n=[int(i) for i in (input().split())]
prin(solve(m,n))