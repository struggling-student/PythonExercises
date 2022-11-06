public class MothTester2
{
   public static void main(String[] args)
   {
      Moth gypsy = new Moth(20);
      gypsy.moveToLight(10);
      System.out.println(gypsy.getPosition());
      System.out.println("Expected: 15.0");
      gypsy.moveToLight(10);
      System.out.println(gypsy.getPosition());
      System.out.println("Expected: 12.5");
      gypsy.moveToLight(-10);
      System.out.println(gypsy.getPosition());
      System.out.println("Expected: 1.25");
      gypsy.moveToLight(0);
      System.out.println(gypsy.getPosition());
      System.out.println("Expected: 0.625");
   }
}
