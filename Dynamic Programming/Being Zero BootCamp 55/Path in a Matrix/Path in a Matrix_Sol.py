"""Given a matrix, find the number of ways to reach from the top-left cell to the right-bottom cell. 
At any step, from the current cell (i,j) you can either move to (i+1,j) or (i,j+1) or (i+1, j+1). 
Please note that certain cells are forbidden and cannot be used.

Input Format

First line of input contains T - number of test cases. 
First line of each test case contains N, M - size of the matrix and B - number of forbidden cells. 
Its followed by B lines each containing a pair (i,j) - index of the forbidden cell.

Constraints

20 points
1 <= N, M <= 10

80 points
1 <= N, M <= 100

General Constraints
1 <= T <= 500
0 <= i < N
0 <= j < M

Output Format

For each test case, print the number of ways, separated by newline. 
Since the output can be very large, print output % 1000000007

Sample Input 0

5
5 2 1
2 0
7 3 1
1 0
6 3 1
5 2
2 9 1
0 1
5 6 2
0 1
1 0
Sample Output 0

4
24
0
2
129

"""

def path():
	
	R,C,B=[int(l) for l in input().split()]
	arr = [[0 for i in range(C)] for j in range(R)]
	for b in range (0,B):
		i,j=[int(l) for l in input().split()]
		arr[i][j]=-1
	
	if(arr[0][0]==-1 or arr[R-1][C-1]==-1):
		return 0

	arr[R-1][C-1]=1
    
    #Last row -->0
	xy=0;
	for i in range(R-1,-1,-1):
		if(arr[i][C-1]==-1):
			arr[i][C-1]=0
			xy=i
			break

		arr[i][C-1]=1

	for i in range (0,xy):
		arr[i][C-1]=0

	#Last column -->0
	xy=0
	for j in range(C-1,-1,-1):
		if(arr[R-1][j]==-1):
			arr[R-1][j]=0
			xy=j
			break

		arr[R-1][j]=1

	for j in range (0,xy):
		arr[R-1][j]=0

	#Main Part.
	for i in range (R-2,-1,-1):
		for j in range(C-2,-1,-1):
			if(arr[i][j]==-1):
				arr[i][j]=0
			else:
				arr[i][j]=((arr[i][j+1]%M+arr[i+1][j]%M)%M+arr[i+1][j+1]%M)%M

	return(arr[0][0]%M)
    
M=1000000007
T=int(input())
while(T>0): 
	print(path())
	T-=1