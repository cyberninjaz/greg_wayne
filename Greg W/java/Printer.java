import java.util.Scanner;
public class Printer {
    public static void main(String [] args) {
        Scanner sc = new Scanner (System.in);
        System.out.print("Ask the printer somethining to print");
        String answer = sc.nextLine();
        System.out.println(answer);

    }
}
