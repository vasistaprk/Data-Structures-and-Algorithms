n=int(input())
count=1;
arr = [[0 for i in range(n)] for j in range(n)]
for i in range(0,n):
    for j in range(0,n):
        if(j<i):
            arr[i][j]=" "
        else:
            arr[i][j]=count
            count+=1
for i in range(0,n):
    for j in range(0,n):
        print(arr[j][i],end=" ")
    print()