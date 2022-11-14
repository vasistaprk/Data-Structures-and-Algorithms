
import java.util.*;

public class Sparse_Matrix_Sol {

    public static void main(String[] args) {
        /* Enter your code here. Read input from STDIN. Print output to STDOUT. Your class should be named Solution. */
        Scanner io =new Scanner(System.in);
        int n= io.nextInt();
        int m= io.nextInt();
        int count=0;
        for(int i=0;i<n;i++){
            for(int j=0;j<m;j++){
                int a=io.nextInt();
                if(a==0){
                    count+=1;
                }
            }
        }
        if(count>((n*m)/2)){
            System.out.println("Yes");
        }
        else{
            System.out.println("No");
        }
    }
}