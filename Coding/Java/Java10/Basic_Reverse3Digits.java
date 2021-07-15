public class Basic_Reverse3Digits {

    public static void main(String[] args) {
	// write your code here
 
    // reverse 3 digit number");

        int input = 127;

        int a = input % 10;
        int b = input / 10 % 10;
        int c = input / 100;
        int output = a * 100 + b * 10 + c;
        System.out.println(output);

    }

}
