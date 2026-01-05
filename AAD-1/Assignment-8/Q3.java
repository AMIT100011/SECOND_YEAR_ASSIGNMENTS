
import java.util.LinkedList;
import java.util.Queue;
import java.util.Stack;

public class Q3 {
  public static void main(String[] args) {
    Stack<Integer> st = new Stack<>();
    Queue<Integer> q = new LinkedList<>();
    st.push(10);
    st.push(20);
    st.push(30);
    System.out.print("Stack elements: ");
    for (Integer i : st) {
      System.out.print(i + " ");
    }
    while (!st.isEmpty()) {
      q.add(st.pop());
    }
    System.out.println();
    System.out.print("Queue elements: ");
    while (!q.isEmpty()) {
      System.out.print(q.remove() + " ");
    }
    System.out.println();
  }
}
