import java.io.*;
public class EmployeeTest{
    public static void main(String[] args){
        Employee empOne = new Employee("A");
        Employee empTwo = new Employee("B");
    
        empOne.empAge(30);
        empOne.empDesignation("Senior");
        empOne.empSalary(2000);
        empOne.printEmployee();
    
        empTwo.empAge(20);
        empTwo.empDesignation("Junior");
        empTwo.empSalary(1000);
        empTwo.printEmployee();
    }

}


/* import java.io.*;
public class EmployeeTest{
 
   public static void main(String[] args){
      //* 使用构造器创建两个对象
      Employee empOne = new Employee("RUNOOB1");
      Employee empTwo = new Employee("RUNOOB2");
 
      // 调用这两个对象的成员方法
      empOne.empAge(26);
      empOne.empDesignation("高级程序员");
      empOne.empSalary(1000);
      empOne.printEmployee();
 
      empTwo.empAge(21);
      empTwo.empDesignation("菜鸟程序员");
      empTwo.empSalary(500);
      empTwo.printEmployee();
   }
} */