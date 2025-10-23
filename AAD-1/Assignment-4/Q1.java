import java.util.Scanner;

public class Q1 {
    public static void checkSorted(int[] arr){
        boolean asc = true;
        boolean des = true;

        for (int i = 1; i < arr.length ; i++) {
            if(arr[i-1] > arr[i]){
                asc = false;
            }
            else {
                des = false;
            }
        }
        if(asc) System.out.println("yes its in ascending order");
        else if(des) System.out.println("yes its in descending order");
        else System.out.println("No");


    }
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("enter the size of array : ");
        int n = sc.nextInt();
        int[] arr = new int[n];
        System.out.println("enter the elements of array : ");
        for (int i = 0; i < n; i++)
            arr[i] = sc.nextInt();

        checkSorted(arr);
    }
}
