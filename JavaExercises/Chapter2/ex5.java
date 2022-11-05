import java.awt.Rectangle;

/**
   Constructs a Rectangle object with area of 42 and another Rectangle object with perimeter 42 and then prints both heights and widths.
*/
public class Rectangles42
{
   public static void main(String[] args)
   {
      Rectangle r1 = new Rectangle(10, 10, 3, 14);
      Rectangle r2 = new Rectangle(30, 30, 10, 11);

      System.out.println("R1 Height: " + r1.getHeight());
      System.out.println("R1 Width: " + r1.getWidth());
      System.out.println("R2 Height: " + r2.getHeight());
      System.out.println("R2 Width: " + r2.getWidth());
   }
}
