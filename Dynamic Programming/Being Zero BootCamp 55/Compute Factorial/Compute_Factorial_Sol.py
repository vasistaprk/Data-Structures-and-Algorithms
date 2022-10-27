"""Given a number N, print N!.

Input Format

First line of input contains T - number of test cases. 
Its followed by T lines, each containing a single number N.

Constraints

1 <= T <= 1000000
0 <= N <= 1000000

Output Format

For each test case, print N!. Since the result can be very large, print N! % 1e9+7.

Sample Input 0

3
5
20
50
Sample Output 0

120
146326063
318608048

"""

M=1000000007
gtfill=1
GT=[]
GT.append(1)
GT.append(1)

x=int(input())

def fact(a):
    if(a==0 or a==1):
        return GT[a]
    
    global gtfill
    if( gtfill >= a):
        return(GT[a])
    
    for i in range(gtfill+1,a+1):
        GT.append(((i%M)*(GT[i-1]%M))%M)
        gtfill+=1
    
    return(GT[a])

for i in range(0,x):
    y=int(input())
    print(fact(y))










