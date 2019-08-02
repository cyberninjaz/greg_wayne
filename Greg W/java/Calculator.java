import java.util.Scanner; 
public class Calculator {
    public static void main(String [] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter two floats");
        double a = sc.nextDouble();
        double b = sc.nextDouble();
        System.out.println(a+b);
        System.out.println(a-b);
        System.out.println(a*b);
        System.out.println(a/b);
        System.out.println(a%b);
    }
}
