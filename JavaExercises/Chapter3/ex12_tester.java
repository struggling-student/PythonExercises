/**
   This program tests the Car class.
*/
public class CarTester
{ 
   public static void main(String [] args)
   { 
      Car myHybrid = new Car(50); // 50 miles per gallon       
      myHybrid.addGas(20); 
      myHybrid.drive(100); // consumes 2 gallons      
      double gasLeft = myHybrid.getGasInTank(); 
      
      System.out.print("Gas left: ");
      System.out.println(gasLeft);
      System.out.println("Expected: 18");
   } 
}
