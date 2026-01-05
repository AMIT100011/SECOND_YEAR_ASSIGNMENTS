
public class Q2 {

    class Node {

        int data;
        Node next;

        Node(int data) {
            this.data = data;
            this.next = null;
        }

    }

    Node front = null;
    Node rear = null;

    void enqueue(int x) {
      Node a = new Node(x);
      if (rear == null) {
        front = rear = a;
        System.out.println(x + " enqueued to queue");
        return;
      }
      rear.next = a;
      rear = a;
      System.out.println(x + " enqueued to queue");

    }

    void dequeue() {
      if (front == null) {
        System.out.println("Queue Underflow");
        return;
      }
      int x = front.data;
      front = front.next;
      if (front == null) {
        rear = null;
      }
      System.out.println(x + " dequeued from queue");
    }
    void display() {
      if (front == null) {
        System.out.println("Queue is empty");
        return;
      }
      System.out.print("Queue elements: ");
      Node temp = front;
      while (temp != null) {
        System.out.print(temp.data + " ");
        temp = temp.next;
      }
      System.out.println();
    }

    public static void main(String[] args) {
      Q2 q = new Q2();
      q.enqueue(10);
      q.enqueue(20);
      q.enqueue(30);
      q.display();
      q.dequeue();
      q.display();
    }
}
