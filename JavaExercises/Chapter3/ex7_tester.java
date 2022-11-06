/**
   Tests the bank account class with interest.
*/
public class BankAccountTester
{  
   public static void main(String[] args)
   {  
      BankAccount momsSavings = new BankAccount(1000);
      momsSavings.addInterest(10);
      
      double balance = momsSavings.getBalance();

      System.out.print("Balance: ");      
      System.out.println(balance);
      System.out.println("Expected: 1100");
   }
}
