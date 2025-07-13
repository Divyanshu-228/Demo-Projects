import java.util.Scanner;

public class BasicsDemo {

    // Method to demonstrate a simple function
    public static int multiply(int a, int b) {
        return a * b;
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        // 1. Hello World
        System.out.println("Hello, World!");

        // 2. User input for basic types
        System.out.print("\nEnter your name: ");
        String name = scanner.nextLine();

        System.out.print("Enter your age: ");
        int age = scanner.nextInt();

        System.out.print("Enter your grade (A/B/C): ");
        char grade = scanner.next().charAt(0);

        System.out.println("\n--- Your Info ---");
        System.out.println("Name: " + name);
        System.out.println("Age: " + age);
        System.out.println("Grade: " + grade);

        // 3. Conditional Statements
        if (age >= 18) {
            System.out.println("You are an adult.");
        } else {
            System.out.println("You are a minor.");
        }

        // 4. Switch statement
        switch (grade) {
            case 'A':
                System.out.println("Excellent performance!");
                break;
            case 'B':
                System.out.println("Good job!");
                break;
            case 'C':
                System.out.println("Needs improvement.");
                break;
            default:
                System.out.println("Invalid grade entered.");
        }

        // 5. Loops
        System.out.println("\nFor Loop: Counting 1 to 5");
        for (int i = 1; i <= 5; i++) {
            System.out.println("Count: " + i);
        }

        System.out.println("\nWhile Loop: Counting 1 to 5");
        int i = 1;
        while (i <= 5) {
            System.out.println("While Count: " + i);
            i++;
        }

        System.out.println("\nDo-While Loop: Counting 1 to 5");
        int j = 1;
        do {
            System.out.println("Do-While Count: " + j);
            j++;
        } while (j <= 5);

        // 6. Array input
        System.out.print("\nHow many numbers do you want to enter? ");
        int n = scanner.nextInt();
        int[] numbers = new int[n];

        System.out.println("Enter " + n + " numbers:");
        for (int k = 0; k < n; k++) {
            numbers[k] = scanner.nextInt();
        }

        System.out.println("You entered:");
        for (int num : numbers) {
            System.out.println(num);
        }

        // 7. Calling a method
        System.out.print("\nEnter two numbers to multiply: ");
        int num1 = scanner.nextInt();
        int num2 = scanner.nextInt();

        int result = multiply(num1, num2);
        System.out.println("Multiplication Result: " + result);

        // Close the scanner
        scanner.close();
    }
}
