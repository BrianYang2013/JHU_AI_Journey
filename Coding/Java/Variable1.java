public class Variable1 {
    // type identifier [ = value][, identifier [= value] ...] ;
    // Examples: 
    int a, b, c;                // 声明三个int型整数：a、 b、c
    int d = 3, e = 4, f = 5;    // 声明三个整数并赋予初值
    byte z = 22;                // 声明并初始化 z
    String s = "runoob";        // 声明并初始化字符串 s
    double pi = 3.14159;        // 声明了双精度浮点型变量 pi
    char x = 'x';               // 声明变量 x 的值是字符 'x'。

    static int allClicks=0;     // 类变量
    String str="hello world";   // 实例变量
    public void method(){
        int i =0;               // 局部变量
    }        

    // ======== local variable ======== 
    public void pupAge(){
       int d = 0;
       d = d + 7;
       System.out.println("小狗的年龄是: " + d);
    }

    public static void main(String[] args){
        //local variable
        Variable1 var1 = new Variable1();
        var1.pupAge();
    }
}
