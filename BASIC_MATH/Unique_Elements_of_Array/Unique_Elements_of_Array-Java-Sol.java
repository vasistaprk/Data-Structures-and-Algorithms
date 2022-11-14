import java.io.*;
import java.util.*;

public class Solution {

    public static void main(String[] args) {
        /* Enter your code here. Read input from STDIN. Print output to STDOUT. Your class should be named Solution. */
        Scanner io = new Scanner(System.in);
        int x=io.nextInt();
        int [] ar = new int[x];
        for(int i=0;i<x;i++){
            ar[i]=io.nextInt();   
        }
        for(int i=0;i<x;i++){
            int count=1;
            for(int j=i+1;j<x;j++){
                if(ar[j]==ar[i] && ar[j]!=-1){
                    count+=1;
                    ar[j]=-1;
                }
            }
            if(count==1 && ar[i]!=-1){
                System.out.print(ar[i]+" ");
            }
        }
    }
}



//Time Complexity: O(N^2)
//Space CVomplexity: O(1)
