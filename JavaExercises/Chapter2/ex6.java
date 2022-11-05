import java.awt.Rectangle;

public class AddTester
{
   public static void main(String[] args)
   {
      Rectangle box = new Rectangle(5, 10, 20, 30);
      box.add(0, 0);

      System.out.println("X: " + box.getX());
      System.out.println("Expected: 0.0");
      System.out.println("Y: " + box.getY());
      System.out.println("Expected: 0.0");
      System.out.println("Height: " + box.getHeight());
      System.out.println("Expected: 40.0");
      System.out.println("Width: " + box.getWidth());
      System.out.println("Expected: 25.0");
   }
}
