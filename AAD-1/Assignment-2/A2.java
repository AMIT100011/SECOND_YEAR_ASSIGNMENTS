
import java.util.Scanner;

public class Experiment2 {

    //  Recursive Sum of n numbers
    static int sumOfN(int n) {
        if (n == 0)
            return 0;
        return n + sumOfN(n - 1);
    }

    // Recursive Factorial
    static int factorial(int n) {
        if (n == 0 || n == 1)
            return 1;
        return n * factorial(n - 1);
    }

    //  Recursive Fibonacci
    static int fibonacci(int n) {
        if (n == 1 || n == 2)
            return 1;
        return fibonacci(n - 1) + fibonacci(n - 2);
    }

    //  Recursive Linear Search
    static int linearSearch(int arr[], int n, int key, int index) {
        if (index == n)
            return -1;
        if (arr[index] == key)
            return index;
        return linearSearch(arr, n, key, index + 1);
    }

    //  Recursive Binary Search
    static int binarySearch(int arr[], int low, int high, int key) {
        if (low > high)
            return -1;

        int mid = (low + high) / 2;
        if (arr[mid] == key)
            return mid;
        else if (key < arr[mid])
            return binarySearch(arr, low, mid - 1, key);
        else
            return binarySearch(arr, mid + 1, high, key);
    }

    // Recursive Decimal to Hexadecimal
    static void decimalToHex(int num) {
        if (num == 0)
            return;
        int remainder = num % 16;
        decimalToHex(num / 16);

        if (remainder < 10)
            System.out.print(remainder);
        else
            System.out.print((char) ('A' + (remainder - 10)));
    }

    // Tower of Hanoi
    static void towerOfHanoi(int n, char from, char aux, char to) {
        if (n == 1) {
            System.out.println("Move disk 1 from " + from + " to " + to);
            return;
        }
        towerOfHanoi(n - 1, from, to, aux);
        System.out.println("Move disk " + n + " from " + from + " to " + to);
        towerOfHanoi(n - 1, aux, from, to);
    }

    // Main Menu
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int choice;

        do {
            System.out.println("\n===== EXPERIMENT - 02 MENU =====");
            System.out.println("1. Sum of n numbers (Recursive)");
            System.out.println("2. Factorial (Recursive)");
            System.out.println("3. Fibonacci (Recursive)");
            System.out.println("4. Linear Search (Recursive)");
            System.out.println("5. Binary Search (Recursive)");
            System.out.println("6. Decimal to Hexadecimal (Recursive)");
            System.out.println("7. Tower of Hanoi");
            System.out.println("8. Exit");
            System.out.print("Enter your choice: ");
            choice = sc.nextInt();

            switch (choice) {
                case 1:
                    System.out.print("Enter n: ");
                    int n1 = sc.nextInt();
                    System.out.println("Sum = " + sumOfN(n1));
                    break;

                case 2:
                    System.out.print("Enter n: ");
                    int n2 = sc.nextInt();
                    System.out.println("Factorial = " + factorial(n2));
                    break;

                case 3:
                    System.out.print("Enter n: ");
                    int n3 = sc.nextInt();
                    System.out.println("Fibonacci number = " + fibonacci(n3));
                    break;

                case 4:
                    System.out.print("Enter number of elements: ");
                    int n4 = sc.nextInt();
                    int arr1[] = new int[n4];
                    System.out.println("Enter array elements:");
                    for (int i = 0; i < n4; i++)
                        arr1[i] = sc.nextInt();
                    System.out.print("Enter element to search: ");
                    int key1 = sc.nextInt();
                    int pos1 = linearSearch(arr1, n4, key1, 0);
                    if (pos1 == -1)
                        System.out.println("Element not found.");
                    else
                        System.out.println("Element found at position: " + (pos1 + 1));
                    break;

                case 5:
                    System.out.print("Enter number of elements: ");
                    int n5 = sc.nextInt();
                    int arr2[] = new int[n5];
                    System.out.println("Enter sorted array elements:");
                    for (int i = 0; i < n5; i++)
                        arr2[i] = sc.nextInt();
                    System.out.print("Enter element to search: ");
                    int key2 = sc.nextInt();
                    int pos2 = binarySearch(arr2, 0, n5 - 1, key2);
                    if (pos2 == -1)
                        System.out.println("Element not found.");
                    else
                        System.out.println("Element found at position: " + (pos2 + 1));
                    break;

                case 6:
                    System.out.print("Enter decimal number: ");
                    int num = sc.nextInt();
                    System.out.print("Hexadecimal: ");
                    if (num == 0)
                        System.out.print("0");
                    else
                        decimalToHex(num);
                    System.out.println();
                    break;

                case 7:
                    System.out.print("Enter number of disks: ");
                    int disks = sc.nextInt();
                    towerOfHanoi(disks, 'A', 'B', 'C');
                    break;

                case 8:
                    System.out.println("Exiting...");
                    break;

                default:
                    System.out.println("Invalid choice! Try again.");
            }

        } while (choice != 8);
    }
}
