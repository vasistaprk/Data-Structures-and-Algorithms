#Taking Input from user.
t=int(input()) #test cases

for l in range(0,t):
    n=int(input()) #Sqaure matrix Size
    #Intialization of matrix
    a=[[0 for i in range(0,n)]for j in range(0,n)]
    for i in range(0,n):
            a[i]=list(map(int, input().split())) #Storing input from user in list.
    
    print("Test Case #"+str(l+1)+":")
    for j in range(0,n):
        for i in range(n-1,-1,-1):
            print(a[i][j],end=" ")
            
        print()

#Had just print the Output and didnt store any rotated matrix.
"""
If you wish to store the output for futher use, Replace code from line 12 with below code:

result_matrix=[]
for j in range(0,n):
    temp=[]
    for i in range(n-1,-1,-1):
        temp.append(a[i][j])
    result_matrix.append(temp)

for i in range(0,n):
    for j in range(0,n):
        print(result_matrix[i][j],end=" ")
    
    print()


NOTE: Make sure the code is inside firsr for loop. "Indentation".             
"""