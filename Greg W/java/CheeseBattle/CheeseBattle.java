import java.util.Random;
import java.util.Scanner;
public class CheeseBattle {
    static void battle(Fighter user, Fighter cpu) {
        Scanner sc = new Scanner(System.in);
        Random rng = new Random();

        System.out.println("The battle has started you are fighting a cheese named " + cpu.name);

        while (user.health > 0 && cpu.health > 0) {
            for (Attack a : user.attacks) {
                System.out.println(a.name);
            }
        
            // let user pick attack
            String userchoice = sc.nextLine();
            Attack attack = null;
            for (Attack a : user.attacks) {
                if( userchoice.equals(a.name)) {
                    attack = a;
                    break;
                }
            }
            
            //user attack
            double RandUserAccuracy = rng.nextDouble();
            if(attack.accuracy < RandUserAccuracy ) {
                System.out.println("Attack misses");
            }
            else {
                cpu.health = cpu.health - attack.damage;
                System.out.println("Cpu.health : " + cpu.health);
                System.out.println("Attack hits!");
            }

            // cpu select attack
            int index = rng.nextInt(cpu.attacks.length);
            Attack cpuAttack = cpu.attacks[index];
            System.out.print("Cpu uses " + cpuAttack.name);


            // cpu uses attack
            double RandCpuAccuracy = rng.nextDouble();
            if(attack.accuracy < RandCpuAccuracy) {
                System.out.println("Attack misses");
            }
            else {
                user.health = user.health - cpuAttack.damage;
                System.out.println("User health : " + user.health);
                System.out.println("Attack hits");
            }
        }
    }
      
    public static void main(String [] args) {
        Fighter user = new Fighter();
        user.defence = 30;
        user.health = 200;
        user.strength = 2;
        user.name = "Mozzarella";
        Attack cheeseroll = new Attack();
        cheeseroll.damage = 20;
        cheeseroll.accuracy = 0.80;
        cheeseroll.name = "cheeseroll";
        Attack bouncinghit = new Attack();
        bouncinghit.damage = 50;
        bouncinghit.accuracy = 0.60;
        bouncinghit.name = "bouncinghit";
        user.attacks = new Attack[] {cheeseroll, bouncinghit};

        Fighter cpu = new Fighter();
        cpu.defence = 20;
        cpu.health = 180;
        cpu.strength = 1; 
        cpu.name = "Spaghetti Monster";
        Attack sauceattack = new Attack();
        sauceattack.damage = 25;
        sauceattack.accuracy = 0.80;
        sauceattack.name = "sauce attack";
        Attack noodlewhack = new Attack();
        noodlewhack.damage = 40;
        noodlewhack.accuracy = 0.60;
        noodlewhack.name = "noodle whack";
        cpu.attacks = new Attack[] {sauceattack, noodlewhack };

        battle(user, cpu);
    }
}

