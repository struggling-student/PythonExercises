/**
   A savings account has a balance that can be changed by 
   deposits and withdrawals.
*/
public class SavingsAccount
{  
   private double balance;
   private double interestRate;

   /**
      Constructs a savings account with a zero balance
   */
   public SavingsAccount()
   {   
      balance = 0;
      interestRate = 0;
   }

   /**
      Constructs a savings account with a given balance
      @param initialBalance the initial balance
      @param rate the interest rate in percent
   */
   public SavingsAccount(double initialBalance, double rate)
   {   
      balance = initialBalance;
      interestRate = rate;
   }

   /**
      Deposits money into the savings account.
      @param amount the amount to deposit
   */
   public void deposit(double amount)
   {  
      double newBalance = balance + amount;
      balance = newBalance;
   }

   /**
      Withdraws money from the savings account.
      @param amount the amount to withdraw
   */
   public void withdraw(double amount)
   {   
      double newBalance = balance - amount;
      balance = newBalance;
   }

   /**
      Gets the current balance of the savings account.
      @return the current balance
   */
   public double getBalance()
   {   
      return balance;
   }

   /**
      Adds interest to the savings account.
   */
   public void addInterest()
   {   
      double interest = balance * interestRate / 100;
      balance = balance + interest;
   }
}
