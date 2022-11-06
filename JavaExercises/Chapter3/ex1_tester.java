public class CounterTester
{
   public static void main(String[] args)
   {
      Counter tally = new Counter();
      tally.click();
      tally.click();
      tally.click();
      System.out.println(tally.getValue());
      System.out.println("Expected: 3");
      tally.undo();
      System.out.println(tally.getValue());
      System.out.println("Expected: 2");
      tally.undo();
      tally.undo();
      tally.undo();
      System.out.println(tally.getValue());
      System.out.println("Expected: 0");
   }
}
