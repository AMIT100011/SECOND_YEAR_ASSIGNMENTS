import java.util.Scanner;

public class Q3 {
    public static int smallest(int[] arr,int k){
        sort(arr);
        return arr[k-1];
    }
    public static void sort(int[] arr){
        int n = arr.length;
        for(int i = 0; i < n - 1; i++){
            for(int j = 0; j < n - i - 1; j++){
                if(arr[j] > arr[j + 1]){
                    int temp = arr[j];
                    arr[j] = arr[j + 1];
                    arr[j + 1] = temp;
                }
            }
        }
    }
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("enter the size of array : ");
        int n = sc.nextInt();
        int[] arr = new int[n];
        System.out.println("enter the elements of array : ");
        for (int i = 0; i < n; i++) {
            arr[i] = sc.nextInt();
        }
        System.out.println("enter key ");
        int k = sc.nextInt();
        if (k >= 1 && k <= n) {
            int kth = smallest(arr, k);
            System.out.println("The " + k + "th smallest element is: " + kth);
        } else {
            System.out.println("Invalid value of k.");
        }

    }

}
