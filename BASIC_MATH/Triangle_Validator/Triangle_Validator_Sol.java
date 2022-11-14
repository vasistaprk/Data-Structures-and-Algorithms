import java.util.*;

public class Triangle_Validator_Sol {
    public static void main(String[] args) {
        try (Scanner io = new Scanner(System.in)) {
            int a = io.nextInt();
            int b = io.nextInt();
            int c = io.nextInt();
            String ans="Yes";
            if(a+b<=c)
                ans="No";
            if(b+c<=a)
                ans="No";
            if(a+c<=b)
                ans="No";
            
            System.out.println(ans);
        }
        
    }
    
}
