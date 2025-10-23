import java.util.Scanner;

public class Q4 {

    public static void findPair(int[] arr) {
        int n = arr.length;
        int totalSum = 0;
        for (int num : arr)
            totalSum += num;

        // If totalSum is odd, no pair exists
        if (totalSum % 2 != 0) {
            System.out.println("No such pair exists.");
            return;
        }

        int target = totalSum / 2;
        boolean found = false;

        // Check all pairs
        for (int i = 0; i < n - 1; i++) {
            for (int j = i + 1; j < n; j++) {
                if (arr[i] + arr[j] == target) {
                    System.out.println("Pair found: (" + arr[i] + ", " + arr[j] + ")");
                    found = true;
                }
            }
        }

        if (!found) System.out.println("No such pair exists.");
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.print("Enter size of array: ");
        int n = sc.nextInt();

        int[] arr = new int[n];
        System.out.println("Enter elements:");
        for (int i = 0; i < n; i++)
            arr[i] = sc.nextInt();

        findPair(arr);
        sc.close();
    }
}
