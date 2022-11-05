/**
   Switches the letters "e" and "o" in a string. Uses the replace method
   repeatedly. "Hello, World!" turns into "Holle, Werld!"
*/
public class HollePrinter
{
   public static void main(String[] args)
   {
      String str = "Hello, World!";

      str = str.replace("e", "%");
      str = str.replace("o", "e");
      str = str.replace("%", "o");

      System.out.println(str);
   }    
}
