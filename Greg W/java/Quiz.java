import java.util.Scanner;


public class Quiz {
    public static void main( String [] args) {
        Scanner sc = new Scanner(System.in);
        int score = 0;

        Question q1 = new Question();
        q1.question = "This is the quiz it will score your wit. Question 1, what are the first 9 digits of pi";
        q1.answer = "3.14159265";
        if (q1.askAndCheck(sc));
            score = score+1 ;
        
        Question q2 = new Question();
        q2.question = "What are the two isotopes of hydrogen in nuclear fusion";
        q2.answer = "deuterium and tritium";
        if (q2.askAndCheck(sc));
            score = score+1;
        
        Question q3 = new Question();
        q3.question = "If you were on a bridge 1500 feet in the air spanned over the ground and it broke and it fell. What should you do?";
        q3.answer = "jump off while it is 5 feet in the air in a diagonal direction off the bridge to get out";
        if (q3.askAndCheck(sc));
            score = score+1;

        Question q4 = new Question();
        q4.question = "Who started the cold war because he wanted to show off?";
        q4.answer = "president truman";
        if (q4.askAndCheck(sc));
            score = score+1;

        Question q5 = new Question();
        q5.question = "What is the highly explosive fuel used for rockets?";
        q5.answer = "liquid hydrogen";
        if (q5.askAndCheck(sc));
            score = score + 1;

        Question q6 = new Question();
        q6.question = "What is the radioactive particle that alters DNA?";
        q6.answer = "beta particles";
        if (q6.askAndCheck(sc));
            score = score + 1;

        Question q7 = new Question();
        q7.question = "What kind of charge do neutrons have?";
        q7.answer = "they don't have one";
        if (q7.askAndCheck(sc));
            score = score + 1;

        Question q8 = new Question();
        q8.question = "What is the most well-known battle in WW1?";
        q8.answer = "ypres";
        if (q8.askAndCheck(sc));
            score = score + 1;

        Question q9 = new Question();
        q9.question = "Linus Pauling prescribed megavitamins to people. What made this cause cancer?";
        q9.answer= "it tipped the oxidation process in favor of antioxidation.";
        if (q9.askAndCheck(sc));
            score = score + 1;

        Question q10 = new Question();
        q10.question = "What is the most dangerous kind of radiation on the electromagnetic spetrum?";
        q10.answer = "cosmic radiation";
        if (q10.askAndCheck(sc))
            score = score + 1;

        if (score == 10)
            System.out.println("Congradulations! You got 100%.Your title is super wise dude.");
        else if (score == 9)
            System.out.println("You scored 90%. Your title is smart guy.");
        else if (score == 8)
            System.out.println("You scored 80%. Your title is moderate dude.");
        else if (score == 7)
            System.out.println("You scored 70%. Your title is ameteur.");
        else if (score == 6)
            System.out.println("You scored 60%. Your title is novice.");
        else if (score < 6)
            System.out.println("You failed.");
    }
}