import java.util.Scanner;

//Given an array of size N. The elements in the array may be repeated. You
//need to find the sum of distinct elements of the array. If there is some value
//repeated then they should be added once.
public class Q10 {
    static boolean isDuplicate(int arr[], int index) {
        for (int i = 0; i < index; i++) {
            if (arr[i] == arr[index])
                return true;
        }
        return false;
    }
    public static int sum(int[] arr){
        int sum = 0;
        for (int i = 0; i < arr.length; i++) {
            if(!isDuplicate(arr,i)){
                sum += arr[i];
            }
        }
        return sum;
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
        int result = sum(arr);
        System.out.println("Sum of distinct elements: " + result);
    }
}
