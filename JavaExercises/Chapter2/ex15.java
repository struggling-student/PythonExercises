import java.awt.Point;

public class PointTester
{
   public static void main(String[] args)
   {
      Point ptA = new Point(3, 4);
      Point ptB = new Point(-3, -4);

      System.out.println("Distance: " + ptA.distance(ptB));
      System.out.println("Expected: 10.0");
   }
}
