public class LetterPrinter
{
   public static void main(String[] args)
   {
      Letter dearJohnLetter = new Letter("Mary", "John");

      dearJohnLetter.addLine("I am sorry we must part.");
      dearJohnLetter.addLine("I wish you all the best.");
      
      System.out.println(dearJohnLetter.getText());
   }
}
