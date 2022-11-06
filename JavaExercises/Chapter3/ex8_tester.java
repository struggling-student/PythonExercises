/**
   Tests the savings account class.
*/
public class SavingsAccountTester
{  
   public static void main(String[] args)
   {  
      SavingsAccount momsSavings = new SavingsAccount(1000, 10);
      
      momsSavings.addInterest();
    
      double balance = momsSavings.getBalance();
      System.out.println("Balance: " + balance);
      System.out.println("Expected: 1100.0");
   }
}
