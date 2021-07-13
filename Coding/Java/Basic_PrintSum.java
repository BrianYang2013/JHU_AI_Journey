public class Basic_PrintSum {

    public static void main(String[] args) {
	// write your code here
        System.out.println("===================");
        System.out.println("print out 0-5");
        System.out.println("===================");
        for (int i = 0; i < 5; i++) {
            System.out.println(i);
        }

        System.out.println("===================");
        System.out.println("print out the sum from 1 to 100");
        System.out.println("===================");

        int sum = 0;
        int n = 100;
        for (int i = 1; i <= n; i++){
            sum += i;
        }
        System.out.println(sum);

    }

}
