/**
   This program tests the replace method of the String class.
 */
public class ReplaceTester
{
   public static void main(String[] args)
   {
      String river = "Mississippi";
		String s1 = river.replace("i", "!");
		String s2 = s1.replace("s", "$");
		System.out.println("Replaced: " + s2);
		System.out.println("Expected: M!$$!$$!pp!");
   }
}
