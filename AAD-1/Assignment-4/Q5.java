import java.util.Arrays;
import java.util.Scanner;

public class Q5 {

    public static int countTriangles(int[] arr) {
        int n = arr.length;
        int count = 0;

        // Sort the array
        Arrays.sort(arr);

        // Fix the third side arr[k], find pairs (arr[i], arr[j]) such that arr[i] + arr[j] > arr[k]
        for (int k = n - 1; k >= 2; k--) {
            int i = 0, j = k - 1;
            while (i < j) {
                if (arr[i] + arr[j] > arr[k]) {
                    // All pairs (i..j-1, j) satisfy the condition
                     count += (j - i);
                    j--;
                } else {
                    i++;
                }
            }
        }

        return count;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.print("Enter number of elements: ");
        int n = sc.nextInt();

        int[] arr = new int[n];
        System.out.println("Enter elements (positive integers):");
        for (int i = 0; i < n; i++) {
            arr[i] = sc.nextInt();
        }

        int totalTriangles = countTriangles(arr);
        System.out.println("Number of triangles that can be formed: " + totalTriangles);

        sc.close();
    }
}
