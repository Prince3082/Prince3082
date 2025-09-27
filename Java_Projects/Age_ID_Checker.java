import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        // Ask for user input
        System.out.print("Enter your age: ");
        int age = sc.nextInt();

        System.out.print("Do you have an ID card? (true/false): ");
        boolean hasId = sc.nextBoolean();

        // Check eligibility using logical AND
        if (age >= 18 && hasId) {
            System.out.println("You can enter the club ✅");
        } else if (age >= 18 && !hasId) {
            System.out.println("You are old enough but need an ID ❌");
        } else {
            System.out.println("You are not old enough ❌");
        }

        sc.close(); // Close scanner to prevent memory leak
    }
}
