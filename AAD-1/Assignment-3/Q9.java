// Given a list n numbers, find the element which appears maximum number
// of times.

import java.util.Scanner;

public class Q9 {
    public static int maxfreq(int[] arr) {
        int maxCount = 0;
        int maxElement = arr[0];
        for (int i = 0; i < arr.length; i++) {
            int count = 0;
            if (arr[i] == -1)
                continue;
            for (int j = 0; j < arr.length; j++) {
                if (arr[i] == arr[j]) {
                    count++;
                }

            }
            if (count > maxCount) {
                maxCount = count;
                maxElement = arr[i];
            }
        }
        return maxElement;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter the size of array:");
        int n = sc.nextInt();
        int arr[] = new int[n];
        System.out.println("Enter the elements of array:");
        for (int i = 0; i < n; i++) {
            arr[i] = sc.nextInt();
        }
        int result = maxfreq(arr);
        System.out.println("The element with maximum frequency is: " + result);

    }
}

