public class Q1 {
  class arrQ {
    int[] queue;
    int front, rear, size;

    arrQ(int capacity) {
      queue = new int[capacity];
      front = -1;
      rear = -1;
      this.size = capacity;
    }

    void enqueue(int x) {
      if (rear == size - 1) {
        System.out.println("Queue Overflow");
        return;
      }
      if (front == -1) {
        front = 0;
      }
      queue[++rear] = x;
      System.out.println(x + " enqueued to queue");

    }

    void dequeue() {
      if (front == -1 || front > rear) {
        System.out.println("Queue Underflow");
        return;
      }
      int x = queue[front++];
      System.out.println(x + " dequeued from queue");
    }
    void display() {
      if (front == -1 || front > rear) {
        System.out.println("Queue is empty");
        return;
      }
      System.out.print("Queue elements: ");
      for (int i = front; i <= rear; i++) {
        System.out.print(queue[i] + " ");
      }
      System.out.println();
    }
  }
  public static void main(String[] args) {
    arrQ q = new Q1().new arrQ(5);
    q.enqueue(10);
    q.enqueue(20);
    q.enqueue(30);
    q.display();
    q.dequeue();
    q.display();
  }
}