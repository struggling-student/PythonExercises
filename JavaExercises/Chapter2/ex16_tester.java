public class DayTester
{

   public static void main(String[] args)
   {
      // Construct a Day object for today (or any day)
      Day day1 = new Day(2012, 10, 31);

      // Set day2 to 10 days added to day1 and print results
      Day day2 = day1.addDays(10);

      // Print results
      System.out.println(day2.daysFrom(day1));
      System.out.println("Expected: 10");
   }
}
