public class Basic_Overvlow {

    public static void main(String[] args) {
	// write your code here
        System.out.println("===================");
        System.out.println("Overflow");
        System.out.println("===================");
        int minValue = Integer.MIN_VALUE;
        int maxValue = Integer.MAX_VALUE;
        System.out.println("Min value of integer is :" + minValue);
        System.out.println("Max value of integer is :" + maxValue);
        int minValueMinus1 = minValue - 1;
        System.out.println("Overview minValue :"+ minValueMinus1);
        int maxValuePlus1 = maxValue + 1;
        System.out.println("Overview maxValue: " + maxValuePlus1);

        double d = 1; // not a good practice. better to use 1.0 to avoid confusion.
        System.out.println(d);
        
    }

}
