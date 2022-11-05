import java.awt.Color;

/**
   This class demonstrates the brighter method of the Color class.
 */
public class BrighterDemo
{
   public static void main(String[] args)
   {
      Color c = new Color(50, 100, 150);
      Color brighterColor = c.brighter();

      System.out.print("Red: ");
      System.out.println(brighterColor.getRed());
      System.out.print("Green: ");
      System.out.println(brighterColor.getGreen());
      System.out.print("Blue: ");
      System.out.println(brighterColor.getBlue());
   }    
}
