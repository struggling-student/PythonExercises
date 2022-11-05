import java.util.Random;

/**
   This program simulates the toss of a die. 
 */
public class DieSimulator
{
   public static void main(String[] args)
   {
      Random generator = new Random();

      System.out.println(generator.nextInt(6) + 1);
   }
}
