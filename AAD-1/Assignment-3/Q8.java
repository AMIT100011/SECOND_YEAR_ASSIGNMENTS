
//Given an array of integers, find the element pair with minimum/maximum
//        difference
import java.util.*;
public class Q8 {
    static void findMinMaxDifference(int arr[], int n) {
        // Sort array for minimum difference
        for (int i = 0; i < n - 1; i++) {
            for (int j = i + 1; j < n; j++) {
                if (arr[i] > arr[j]) {
                    int temp = arr[i];
                    arr[i] = arr[j];
                    arr[j] = temp;
                }
            }
        }
        // Maximum difference
        int maxDiff = arr[n - 1] - arr[0];
        System.out.println("Maximum difference: " + maxDiff);
        System.out.println("Pair with maximum difference: (" + arr[0] + ", " + arr[n - 1] + ")");

        // Minimum difference
        int minDiff = arr[1] - arr[0];
        for (int i = 1; i < n - 1; i++) {
            int diff = arr[i + 1] - arr[i];
            if (diff < minDiff)
                minDiff = diff;
        }

        System.out.println("Minimum difference: " + minDiff);
        System.out.print("Pair(s) with minimum difference: ");
        for (int i = 0; i < n - 1; i++) {
            if (arr[i + 1] - arr[i] == minDiff)
                System.out.print("(" + arr[i] + ", " + arr[i + 1] + ") ");
        }
        System.out.println();
    }


    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.print("Enter number of elements: ");
        int n = sc.nextInt();

        int arr[] = new int[n];
        System.out.println("Enter " + n + " elements:");
        for (int i = 0; i < n; i++)
            arr[i] = sc.nextInt();

        findMinMaxDifference(arr, n);
    }
}
