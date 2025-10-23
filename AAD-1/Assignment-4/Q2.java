import java.util.Scanner;

public class Q2 {
    private static void findPairsCandidateMethod(int value, int[] x, int[] y) {
        System.out.println("Pairs with absolute difference " + value + ":");
        boolean found = false;
        for (int k : x) {
            for (int i : y) {
                if (Math.abs(k - i) == value) {
                    System.out.println("(" + k + ", " + i + ")");
                    found = true;
                }
            }
        }
    }
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.print("Enter VALUE: ");
        int value = sc.nextInt();

        System.out.print("Enter size of X: ");
        int n = sc.nextInt();
        int[] X = new int[n];
        System.out.println("Enter elements of X:");
        for (int i = 0; i < n; i++) X[i] = sc.nextInt();

        System.out.print("Enter size of Y: ");
        int m = sc.nextInt();
        int[] Y = new int[m];
        System.out.println("Enter elements of Y:");
        for (int i = 0; i < m; i++) Y[i] = sc.nextInt();

        findPairsCandidateMethod(value, X, Y);

    }
}
