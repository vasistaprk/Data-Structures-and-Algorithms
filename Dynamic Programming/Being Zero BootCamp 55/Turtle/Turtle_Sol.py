"""There is a turtle in the left top corner of rectangular table of size n × m. 
Each cell of the table contains some amount of acid. 
Turtle can move right or down, its route terminates in right bottom cell of the table.

Each milliliter of acid brings turtle some amount of damage. 
Find the smallest possible value of damage that will receive a turtle after a walk through the table.

Input
First line contains two positive integers n and m, no more than 1000 - the sizes of the table. 
Then n lines are given, each contains m integers - the description of the table, each number given the amount of acid in the cell (in milliliters).

Output
Print the minimum possible damage for the turtle."""


import sys

def prin(a):
    sys.stdout.write(str(a)+'\n')
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
            arr[i][j]+=min(arr[i][j+1],arr[i+1][j])

    return(arr[0][0])


R,C=[int(i) for i in input().split()]
prin(solve(R,C))