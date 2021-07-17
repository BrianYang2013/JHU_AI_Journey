import java.io.*;

// instance variable
public class Variable2{
   // 这个实例变量对子类可见
   public String name;
   // 私有变量，仅在该类可见
   private double salary;
   //在构造器中对name赋值
   public Variable2 (String empName){
      name = empName;
   }
   //设定salary的值
   public void setSalary(double empSal){
      salary = empSal;
   }  
   // 打印信息
   public void printEmp(){
      System.out.println("Name : " + name );
      System.out.println("Salary : " + salary);
   }
 
   public static void main(String[] args){
      Variable2 empOne = new Variable2("TestName");
      empOne.setSalary(1000.0);
      empOne.printEmp();
   }
}