
import java.util.*;

public class Q2 {

  public static void remove(ArrayList<Integer> arr) {

    while (true) {
      boolean allZero = true;
      for (int num : arr) {
        if (num != 0) {
          allZero = false;
          break;
        }
      }
      if (allZero) {
        break;
      }

      int min = minimum(arr);

      for (int i = 0; i < arr.size(); i++) {
        if (arr.get(i) != 0) {
          arr.set(i, arr.get(i) - min);
        }
      }

      System.out.println(arr);
    }
  }

  public static int minimum(ArrayList<Integer> arr) {
    int min = Integer.MAX_VALUE;
    for (int num : arr) {
      if (num != 0 && num < min) {
        min = num;
      }
    }
    return min;
  }

  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    System.out.println("Enter the size: ");
    int n = sc.nextInt();
    ArrayList<Integer> arr = new ArrayList<>();
    for (int i = 0; i < n; i++) {
      arr.add(sc.nextInt());
    }
    remove(arr);

  }
}
// import java.util.*;

// public class Q2_ArrayVersion {

//     public static void remove(int[] arr) {

//         while (true) {
//             boolean allZero = true;
//             for (int num : arr) {
//                 if (num != 0) {
//                     allZero = false;
//                     break;
//                 }
//             }
//             if (allZero) {
//                 break;
//             }

//             int min = minimum(arr);

//             for (int i = 0; i < arr.length; i++) {
//                 if (arr[i] != 0) {
//                     arr[i] = arr[i] - min;
//                 }
//             }

//             // Print the array
//             System.out.print("[");
//             for (int i = 0; i < arr.length; i++) {
//                 System.out.print(arr[i]);
//                 if (i < arr.length - 1) {
//                     System.out.print(", ");
//                 }
//             }
//             System.out.println("]");
//         }
//     }

//     public static int minimum(int[] arr) {
//         int min = Integer.MAX_VALUE;
//         for (int num : arr) {
//             if (num != 0 && num < min) {
//                 min = num;
//             }
//         }
//         return min;
//     }

//     public static void main(String[] args) {
//         Scanner sc = new Scanner(System.in);
//         System.out.println("Enter the size: ");
//         int n = sc.nextInt();
//         int[] arr = new int[n];
//         for (int i = 0; i < n; i++) {
//             arr[i] = sc.nextInt();
//         }
//         remove(arr);
//     }
// }
