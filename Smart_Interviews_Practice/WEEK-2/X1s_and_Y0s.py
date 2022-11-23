"""
Given two numbers X and Y.
Create a Number  Which has X 1's followed by Y 0's.


Brute Force Method-1:
int solve (int x and int y){
    int r=1
    for i=0 to x:
        r=(r<<1)|1
    return (r<<y)

Brute Force Method-2:
int solve (int x and int y){
    int r=0
    for (i=y; i<=x+y-1; i++){
        r=r+(1<<i);
    }
    return r
       
}
"""

def solve(x,y):
    return (((1<<x)-1)<<y)
    """
    (1<<x)-1 = 2^x -1 --> This will give us X 1's in binary representation
    Eg: 2^2 -1 = 3 --> 0011
        2^3 -1 = 7 --> 0111
        2^4 -1 = 15 --> 1111
        2^5 -1 = 31 --> 0001 1111
    (<<y) --> this will append Y 0's to binary.
    """

x,y=map(int.input().split())
print(solve(x,y))

"""
Similar Solutions: 
1. return (((1<<x)-1)<<y)
2. return (1<<(x+y)-(1<<y))
    If we observe both 1 and 2 are same.
3. return ((1<<(x+y))-1)^((1<<y)-1)
    In this method, we first make x+y 1's to binary and change last y 1's to 0's using XOR operation.
"""