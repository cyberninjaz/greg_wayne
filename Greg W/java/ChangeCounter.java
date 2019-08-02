import java.util.Scanner;
public class ChangeCounter {
    public static void main (String [] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter the amount of cents you have");
        int cents = sc.nextInt();
        int dollars = (cents/100);
        cents = (cents%100);   
        int quarters = (cents/25);
        cents = (cents%25);
        int dimes = (cents/10);
        cents = (cents%10);
        int nickels = (cents/5);
        cents = (cents%5);
        System.out.printf("Your change equals %s dollars and %s quarters %s dimes %s nickels %s cents \n", dollars, quarters, dimes, nickels, cents);
    }
}

