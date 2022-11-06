/** 
    A car can drive and consume fuel. 
*/ 
public class Car 
{ 
   private double gas;
   private double efficiency;

   /** 
      Constructs a car with a given fuel efficiency. 
      @param anEfficiency the fuel efficiency of the car 
   */ 
   public Car(double anEfficiency) 
   {
      gas = 0;
      efficiency = anEfficiency;
   }

   /** Adds gas to the tank. 
       @param amount the amount of fuel to add 
   */ 
   public void addGas(double amount) 
   { 
      gas = gas + amount;
   } 

   /** 
       Drives a certain amount, consuming gas. 
       @param distance the distance driven 
   */ 
   public void drive(double distance) 
   { 
      gas = gas - distance / efficiency;
   } 

   /** 
       Gets the amount of gas left in the tank. 
       @return the amount of gas 
   */ 

   public double getGasInTank() 
   { 
      return gas;
   } 
}
