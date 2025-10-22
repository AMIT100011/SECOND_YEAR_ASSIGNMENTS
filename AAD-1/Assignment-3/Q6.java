
import java.util.Scanner;

//print duplicates

public class Q6 {
  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    System.out.println("Enter the size of array:");
    int n = sc.nextInt();
    int arr[] = new int[n];
    System.out.println("Enter the elements of array:");
    for (int i = 0; i < n; i++) {
      arr[i] = sc.nextInt();
    }
    System.out.println("Duplicate elements are:");
    boolean foundDuplicate = false;
    for (int i = 0; i < n; i++) {
      for (int j = i + 1; j < n; j++) {
        if (arr[i] == arr[j]) {
          System.out.println(arr[i]);
          foundDuplicate = true;
          break; // To avoid printing the same duplicate multiple times
        }
      }
    }
    if (!foundDuplicate) {
      System.out.println("No duplicate elements found");
    }
  }
}
