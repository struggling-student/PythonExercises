public class CounterTester
{
   public static void main(String[] args)
   {
      Counter tally = new Counter();
      tally.setLimit(3);
      tally.click();
      tally.click();
      tally.click();
      System.out.println(tally.getValue());
      System.out.println("Expected: 3");
      tally.click();
      System.out.println(tally.getValue());
      System.out.println("Expected: 3");
   }
}
