/**
   Tests the CashRegister class.
*/
public class CashRegisterDemo
{
   public static void main(String[] args)
   {
      CashRegister register = new CashRegister();

      register.recordPurchase(29.50);
      register.recordPurchase(9.25);

      register.printReceipt();
   }
}
