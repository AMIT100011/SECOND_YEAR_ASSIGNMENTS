import java.util.Scanner;

public class Q4 {
    private static boolean checkReverse(int[] arr, int n) {
        int start = -1;int end = -1;
        for (int i = 0; i < arr.length ; i++) {
            if(arr[i] > arr[i+1]){
                start = i;
                break;
            }
        }
        if(start == -1) return true;

        for (int i = n - 1; i > 0; i--) {
            if (arr[i - 1] > arr[i]) {
                end = i;
                break;
            }
        }
        reverse(arr, start, end);

        // Step 4: check if array is sorted now
        for (int i = 0; i < n - 1; i++) {
            if (arr[i] > arr[i + 1])
                return false;
        }

        return true;
    }
    public static void reverse(int[] arr,int start,int end){
        while(start <= end){
            int temp = arr[start];
            arr[start] = arr[end];
            arr[end] = temp;
            start++;end--;
        }
    }
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.print("Enter number of elements: ");
        int n = sc.nextInt();

        int arr[] = new int[n];
        System.out.println("Enter " + n + " elements:");
        for (int i = 0; i < n; i++)
            arr[i] = sc.nextInt();

        if (checkReverse(arr, n))
            System.out.println("True");
        else
            System.out.println("False");
    }


}
