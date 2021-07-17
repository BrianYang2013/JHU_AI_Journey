
public class Puppy{
   int puppyAge;
   public Puppy(String name){
      System.out.println("小狗的名字是：" + name);
   }

   public void setAge(int age){
      puppyAge = age;
   }

   public int getAge(){
      System.out.println("小狗的年龄是：" + puppyAge);
      return puppyAge;
   }

   public static void main(String[] args){
      Puppy myPuppy = new Puppy("Tommy");
      myPuppy.setAge(2);
      myPuppy.getAge();
      System.out.println("variable: " + myPuppy.puppyAge);
   }
}

/**************************************************************/
/* public class Puppy{
   int puppyAge;
   public Puppy(String name){
      // 这个构造器仅有一个参数：name
      System.out.println("小狗的名字是 : " + name ); 
   }
 
   public void setAge( int age ){
       puppyAge = age;
   }
 
   public int getAge( ){
       System.out.println("小狗的年龄为 : " + puppyAge ); 
       return puppyAge;
   }
 
   public static void main(String[] args){
      // 创建对象
      Puppy myPuppy = new Puppy( "tommy" );
      // 通过方法来设定age
      myPuppy.setAge( 2 );
      // 调用另一个方法获取age 
      myPuppy.getAge( );
      //你也可以像下面这样访问成员变量 
      System.out.println("变量值 : " + myPuppy.puppyAge ); 
   }
}
 */