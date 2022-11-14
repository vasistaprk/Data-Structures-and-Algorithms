import java.util.*;

public class Check_Bit_Sol {
    public static void main(String[] args) {
        /* Enter your code here. Read input from STDIN. Print output to STDOUT. Your class should be named Solution. */
        Scanner io = new Scanner(System.in);
        int x = io.nextInt();
        int i = io.nextInt();
        if(((x>>i)&((int)1))==1){
            System.out.println("true");
        }
        else{
            System.out.println("false");
        }
    }
    
}
