import java.util.Scanner;

public class Calculator {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.println("==== Simple Java Calculator ====");

        // Ask for first number
        System.out.print("Enter first number: ");
        double num1 = sc.nextDouble();

        // Ask for second number
        System.out.print("Enter second number: ");
        double num2 = sc.nextDouble();

        // Ask for operation
        System.out.println("Choose operation: +, -, *, /");
        System.out.print("Enter operator: ");
        char operator = sc.next().charAt(0);

        double result;

        // Perform calculation
        if (operator == '+') {
            result = num1 + num2;
        } else if (operator == '-') {
            result = num1 - num2;
        } else if (operator == '*') {
            result = num1 * num2;
        } else if (operator == '/') {
            if (num2 != 0) {
                result = num1 / num2;
            } else {
                System.out.println("Error: Division by zero!");
                sc.close();
                return; // exit program
            }
        } else {
            System.out.println("Invalid operator!");
            sc.close();
            return; // exit program
        }

        // Print the result
        System.out.println("Result: " + result);

        sc.close(); // close scanner
    }
}
