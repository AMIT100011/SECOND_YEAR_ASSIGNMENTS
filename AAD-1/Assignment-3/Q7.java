
import java.util.Scanner;


// Find the missing number in an array
// Problem: In a given list of n-1 elements, which are in the range of 1 to n.
// There are no duplicates in the array. One of the integers is missing. Find
// the missing element.
public class Q7 {

    public static int missing(int[] arr) {
        int n = arr.length + 1;
        int total = n * (n + 1) / 2;
        int sum = 0;
        for (int num : arr) {
            sum += num;
        }
        return total - sum;//math process
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter the size of array:");
        int n = sc.nextInt();
        int arr[] = new int[n - 1];
        System.out.println("Enter the elements of array:");
        for (int i = 0; i < n - 1; i++) {
          arr[i] = sc.nextInt();
        }
        int missingNumber = missing(arr);
        System.out.println("The missing number is: " + missingNumber);

    }
}
