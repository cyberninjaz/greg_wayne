import java.util.Scanner;
public class OldQuiz {
    public static void main (String [] Args){
        Scanner sc = new Scanner (System.in);
        int score = 0;
        System.out.println("This is the Quiz. Try your best and you will be rewarded but if you fail you will remember your defeat forever. There are 10 questions and then the computer will give you the grade and the proctor will give you your IQ.");
        System.out.println("The first question is what are the first 9 digits of pi?");
        String a = sc.nextLine();
        if ( a.equals("3.14159265")) {
            System.out.println("Correct");
            score = score+1;
        }
        else
            System.out.println("Wrong");
        System.out.println("What are the two isotopes of hydrogen that begin nuclear fusion?");
        String b = sc.nextLine();
        if ( b.equals("deuterium and tritium")) {
            System.out.println("Correct");
            score = score+1;
        }
        else
            System.out.println("Wrong");
        System.out.println("If you were on a bridge 1500 feet in the air spanned over the ground and it broke and it fell. What should you do?");
        String c = sc.nextLine();
        if ( c.equals("jump off while it is 5 feet in the air in a diagonal direction off the bridge to get out")) {
            System.out.println("Correct");
            score = score+1;
        }
        else
            System.out.println("Wrong you may escape with serious injuries or die.");
        System.out.println("Who started the cold war because he wanted to show off.");
        String d = sc.nextLine();
        if ( d.equals("president truman")) {
            System.out.println("Correct");
            score = score+1;
        }
        else
            System.out.println("Wrong");
        System.out.println("What is the highly explosive fuel used for rockets?");
        String e = sc.nextLine();
        if ( e.equals("liquid hydrogen")) {
            System.out.println("Correct");
            score = score+1;
        }
        else
            System.out.println("Wrong");
        System.out.println("What is the radioactive particle that alters DNA?");
        String f = sc.nextLine();
        if ( f.equals("beta particles")) {
            System.out.println("Correct");
            score = score+1;
        }
        else
            System.out.println("Wrong"); 
        System.out.println("What kind of charge does a neutron have?");
        String g = sc.nextLine();
        if (g.equals("They don't have a charge")) {
            System.out.println("Correct");
            score = score+1;
        }
        else
            System.out.println("Wrong");
        System.out.println("What is the most well known battle in WW1?");
        String h = sc.nextLine();
        if (h.equals("ypres")){
            System.out.println("Correct");
            score = score+1;
        }
        else
            System.out.println("Wrong")
        System.out.println
    }   
}



