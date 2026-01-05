
import java.util.LinkedList;
import java.util.Queue;

public class Q4 {
  public static void maxSlidingWindow(int[] arr, int k) {
    int n = arr.length;
    Queue<Integer> q = new LinkedList<>();
    for (int i = 0; i < n; i++) {
      if (q.isEmpty()) {
        q.add(i);
      } else {
        while (!q.isEmpty() && arr[q.peek()] < arr[i]) {
          q.remove();
        }
        q.add(i);
      }
      if (i >= k - 1) {
        System.out.print(arr[q.peek()] + " ");
      }
    }
  }

    public static void main(String[] args) {
        int[] arr = {1, 3, -1, -3, 5, 3, 6, 7};
        int k = 3;

        maxSlidingWindow(arr, k);
    }
}
