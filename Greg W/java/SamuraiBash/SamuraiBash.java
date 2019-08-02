import java.util.Random;
import java.util.Scanner;
public class SamuraiBash {
    static void battle(Fighter user, Fighter cpu) {
        Scanner sc = new Scanner(System.in);
        Random rng = new Random();

        System.out.println("The battle has started you are fighting a ninja named " + cpu.name);

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
        user.health = 100;
        user.strength = 2;
        user.name = "Bob";
        Attack bonablade = new Attack();
        bonablade.damage = 20;
        bonablade.accuracy = 0.80;
        bonablade.name = "Bonablade";
        Attack shotgun = new Attack();
        shotgun.damage = 50;
        shotgun.accuracy = 0.60;
        shotgun.name = "Shotgun";
        user.attacks = new Attack[] {bonablade, shotgun};

        Fighter cpu = new Fighter();
        cpu.defence = 20;
        cpu.health = 90;
        cpu.strength = 1; 
        cpu.name = "Evan";
        Attack sastab = new Attack();
        sastab.damage = 25;
        sastab.accuracy = 0.80;
        sastab.name = "Sastab";
        Attack jorifle = new Attack();
        jorifle.damage = 40;
        jorifle.accuracy = 0.60;
        jorifle.name = "jorifle";
        cpu.attacks = new Attack[] {sastab, jorifle};

        battle(user, cpu);
    }
}

