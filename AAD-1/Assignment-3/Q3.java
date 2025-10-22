
import java.util.*;

public class Q3 {

    public static void merge(int[] arr1, int[] arr2, int m, int n) {
        int left = m - 1;
        int right = n - 1;
        int k = m + n - 1;
        for (int j = k; j >= 0; j++) {
            if (right < 0) {
                break;
            }
            if (left >= 0 && arr1[left] > arr2[right]) {
                arr1[k--] = arr1[left--];
            } else {
                arr1[k--] = arr2[right--];
            }
        }
        while (k >= 0) {
            if (right < 0) {
                break;
            }
            arr1[k--] = arr2[right--];
        }
        System.out.println("Merged array:");
        for (int i = 0; i < m + n; i++) {
            System.out.print(arr1[i] + " ");
        }
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter the size of array 1:");
        int n1 = sc.nextInt();
        System.out.println("Enter the size of array 2:");
        int n2 = sc.nextInt();
        int arr1[] = new int[n1 + n2];
        int arr2[] = new int[n2];

        System.out.println("Enter the elements of array 1:");
        for (int i = 0; i < n1; i++) {
            arr1[i] = sc.nextInt();
        }

        System.out.println("Enter the elements of array 2:");
        for (int i = 0; i < n2; i++) {
            arr2[i] = sc.nextInt();
        }
        merge(arr1, arr2, n1, n2);
    }
}
