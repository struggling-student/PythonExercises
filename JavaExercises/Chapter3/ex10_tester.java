/**
   A class to test the CashRegister class.
*/
public class CashRegisterTester
{
   public static void main(String[] args)
   {
      CashRegister register = new CashRegister();

      // transaction #1
      register.recordPurchase(30);
      register.recordPurchase(10);
      register.recievePayment(50);
      System.out.println("Change for customer 1: " + register.giveChange());
      System.out.println("Expected: 10.0");

      // transaction #2
      register.recordPurchase(20);
      register.recievePayment(10);
      register.recievePayment(10);
      System.out.println("Change for customer 2: " + register.giveChange());
      System.out.println("Expected: 0.0");

      // test new functionality
      System.out.println("Total amt of sales: " + register.getSalesTotal());
      System.out.println("Expected: 60.0");
      System.out.println("Count of sales: " + register.getSalesCount());
      System.out.println("Expected: 2");

      register.reset();
      System.out.println("Total amt of sales: " + register.getSalesTotal());
      System.out.println("Expected: 0.0");
      System.out.println("Count of sales: " + register.getSalesCount());
      System.out.println("Expected: 0");

   }
