/**
   This program tests the Employee class.
*/
public class EmployeeTester
{  
   public static void main(String[] args)
   {  
      Employee harry = new Employee("Harry Hacker", 50000);
      harry.raiseSalary(10);

      System.out.println(harry.getName());
      System.out.println("Expected: Harry Hacker");

      System.out.println(harry.getSalary());
      System.out.println("Expected: 55000");
   }
}
