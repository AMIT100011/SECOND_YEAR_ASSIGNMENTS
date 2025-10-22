import java.util.Scanner;

public class Experiment1 {

    // Function 1: Sum of n numbers
    static void sumOfN() {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter number of elements: ");
        int n = sc.nextInt();
        int sum = 0;
        System.out.println("Enter " + n + " numbers:");
        for (int i = 0; i < n; i++) {
            int num = sc.nextInt();
            sum += num;
        }
        System.out.println("Sum of " + n + " numbers = " + sum);
    }

    // Function 2: Factorial
    static void factorial() {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter a number: ");
        int n = sc.nextInt();
        long fact = 1;
        for (int i = 1; i <= n; i++) {
            fact *= i;
        }
        System.out.println("Factorial of " + n + " = " + fact);
    }

    // Function 3: Nth Fibonacci number
    static void fibonacci() {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter n (for nth Fibonacci number): ");
        int n = sc.nextInt();

        if (n == 1 || n == 2) {
            System.out.println("Fibonacci number = 1");
            return;
        }

        int a = 1, b = 1, c = 0;
        for (int i = 3; i <= n; i++) {
            c = a + b;
            a = b;
            b = c;
        }
        System.out.println("Fibonacci number = " + c);
    }

    // Function 4: Linear Search
    static void linearSearch() {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter number of elements: ");
        int n = sc.nextInt();
        int arr[] = new int[n];
        System.out.println("Enter array elements:");
        for (int i = 0; i < n; i++)
            arr[i] = sc.nextInt();

        System.out.print("Enter element to search: ");
        int key = sc.nextInt();

        boolean found = false;
        for (int i = 0; i < n; i++) {
            if (arr[i] == key) {
                System.out.println("Element found at position: " + (i + 1));
                found = true;
                break;
            }
        }
        if (!found)
            System.out.println("Element not found.");
    }

    // Function 5: Binary Search (array must be sorted)
    static void binarySearch() {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter number of elements: ");
        int n = sc.nextInt();
        int arr[] = new int[n];
        System.out.println("Enter sorted array elements:");
        for (int i = 0; i < n; i++)
            arr[i] = sc.nextInt();

        System.out.print("Enter element to search: ");
        int key = sc.nextInt();

        int low = 0, high = n - 1;
        boolean found = false;
        while (low <= high) {
            int mid = (low + high) / 2;
            if (arr[mid] == key) {
                System.out.println("Element found at position: " + (mid + 1));
                found = true;
                break;
            } else if (arr[mid] < key)
                low = mid + 1;
            else
                high = mid - 1;
        }

        if (!found)
            System.out.println("Element not found.");
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int choice;

        do {
            System.out.println("\n===== EXPERIMENT - 01 MENU =====");
            System.out.println("1. Sum of n numbers");
            System.out.println("2. Factorial of a number");
            System.out.println("3. Nth Fibonacci number");
            System.out.println("4. Linear Search");
            System.out.println("5. Binary Search");
            System.out.println("6. Exit");
            System.out.print("Enter your choice: ");
            choice = sc.nextInt();

            switch (choice) {
                case 1:
                    sumOfN();
                    break;
                case 2:
                    factorial();
                    break;
                case 3:
                    fibonacci();
                    break;
                case 4:
                    linearSearch();
                    break;
                case 5:
                    binarySearch();
                    break;
                case 6:
                    System.out.println("Exiting...");
                    break;
                default:
                    System.out.println("Invalid choice! Try again.");
            }
        } while (choice != 6);
    }
}

