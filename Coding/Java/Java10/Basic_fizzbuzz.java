public class Basic_fizzbuzz {

    public static void main(String[] args) {
	// write your code here
    // fizz buzz

        int m = 30;

        for (int i = 1; i <= m; i++) {
            if (i % 3 == 0 && i % 5 == 0) {
                System.out.println("fizz buzz");
            } else if (i % 3 == 0) {
                System.out.println("fizz");
            } else if (i % 5 == 0) {
                System.out.println("buzz");
            } else {
                System.out.println(i);
            }
        }
    }

}
