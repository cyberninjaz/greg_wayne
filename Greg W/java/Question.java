import java.util.Scanner;

public class Question {
    String question;
    String answer;

    boolean askAndCheck (Scanner sc) {
        System.out.print (question);
        String a = sc.nextLine();
        if ( a.equals(answer)) {
            System.out.println("Correct");
            return true;
        
        } else {
           return false;
        }
    }
}