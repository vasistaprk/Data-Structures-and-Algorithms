"""Hodja Nasreddin is located in the upper left corner of the table of the size n × n, and his donkey is 
located in the lower right corner. Hodge goes only to the right or down, a donkey goes only to the left or up.

In how many ways they can meet in one cell? 
(Two ways are considered different if Hodja or donkey has different routes).

Input
One integer n (1 ≤ n ≤ 50).

Output
Print one number - the number of ways Hodja and donkey can meet. 
This number can be big, so print its value modulo 9929.

"""

M=9929
N=int(input())
Hodja = [[1 for i in range(N)] for j in range(N)]
for i in range (N-2,-1,-1):
    for j in range(N-2,-1,-1):
        Hodja[i][j]=(Hodja[i][j+1]%M+Hodja[i+1][j]%M)%M

Donkey = [[1 for i in range(N)] for j in range(N)]
for i in range (1,N):
    for j in range(1,N):
        Donkey[i][j]=(Donkey[i][j-1]%M+Donkey[i-1][j]%M)%M
sum=0
for i in range (0,N):
    for j in range(0,N):
        x=((Donkey[i][j]%M)*(Hodja[i][j]%M))%M
        sum=((sum%M)+(x%M))%M

print(sum)