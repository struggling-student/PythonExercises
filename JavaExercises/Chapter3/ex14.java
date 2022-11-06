/**
   This class models a simple letter.
 */
public class Letter
{
   private String sender;
   private String recipient;
   private String body;

   /**
      Constructs a letter with a given sender and recipient.
      @param from the sender
      @param to the recipient
   */
   public Letter(String from, String to)
   {
      sender = from;
      recipient = to;      
      body = "";
   }
   
   /**
      Adds a line to the body of this letter. 
   */   
   public void addLine(String line)
   {
      body = body.concat(line).concat("\n");
   }
   
   /**
      Gets the body of this letter.
   */
   public String getText() 
   {
      return "Dear ".concat(recipient).concat(":\n\n").concat(body)
         .concat("\nSincerely,\n\n").concat(sender);
   }
}
