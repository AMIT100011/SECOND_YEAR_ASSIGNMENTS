import java.util.LinkedList;
import java.util.Queue;

public class Q5 {

  static int josephus(int n, int k) {
    Queue<Integer> q = new LinkedList<>();
    for (int i = 0; i < n; i++) {
      q.add(i + 1);

    }
    while (q.size() > 1) {
      for (int i = 0; i < k; i++) {
        q.add(q.remove());

      }
      q.remove();
    }
    return q.peek();
  }

  public static void main(String[] args) {
    int n = 7;
    int k = 3;

    System.out.println("Safe Position: " + josephus(n, k));
  }
}
// static int josephus(int n, int k) {
//     if (n == 1) {
//         return 0;
//     }

//     return (josephus(n - 1, k) + k) % n;
// }

//     public static void main(String[] args) {
//     int n = 7;
//     int k = 3;

//     int safePosition = josephus(n, k) + 1;
//     System.out.println("Safe Position: " + safePosition);
// }
