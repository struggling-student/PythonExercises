/**
   This class models a tally counter.
*/
public class Counter
{
   private int value;
   private int max;

   /**
      Sets the tally limit.
      @param maximum Admission limit.
   */
   public void setLimit(int maximum)
   {
      max = maximum;
   }

   /**
      Gets the current value of this counter.
      @return the current value
   */
   public int getValue()
   {
      return value;
   }

   /**
      Advances the value of this counter by 1.
   */
   public void click()
   {
      value = Math.min(value + 1, max);
   }

   /**
      Resets the value of this counter to 0.
   */
   public void reset()
   {
      value = 0;
   }
}
