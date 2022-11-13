#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main() {

    int n,i,j,m;long long arr[100][100];
    scanf("%d %d",&n,&m);
    for(i=0;i<n;i++)
    {
        for(j=0;j<m;j++)
        {
            scanf("%lld",&arr[i][j]);
        }
    }
    for(i=0;i<m;i++)
    {
        for(j=0;j<n;j++)
        {
            printf("%lld ",arr[j][i]);
        }
        printf("\n");       
                
    }
}

//Time Complexity = O(N*M)
//Space Complexity= O(N*M)