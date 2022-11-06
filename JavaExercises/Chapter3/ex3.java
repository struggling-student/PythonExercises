import java.util.Scanner;

/**
 *
 * Defines an integer range for navigating between
 *
 */
class RangeInput
{

    int min;  // minumum value for the range
    int max;  // maximum value for the range
    int current; // current value within the range

    /**
     *
     * @return the current member within the range
     */
    public int getCurrent()
    {
        return current;
    }

    /**
     * Create a range
     *
     * @param lower the lower bound of the range
     * @param upper the upper bound of the range
     */
    public RangeInput(int lower, int upper)
    {
        min = lower;
        max = upper;
        current = (lower + upper) / 2;
    }

    /**
     * Move the current up if not at the upper bound of the range
     */
    public void up()
    {
        if (Math.max(current + 1, max) == max)
        {
            current++;
        }
    }

    /**
     * Move the current down if not at the lower bound of the range
     */
    public void down()
    {
        if (Math.min(current - 1, min) == min)
        {
            current--;
        }
    }

}

public class E3_3
{

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args)
    {
        Scanner in = new Scanner(System.in);
        int lower;
        int upper;
        System.out.println("This program illustrates constructing and staying within a range of values\n");
        System.out.println("Enter the lower and upper bound for your range");
        System.out.println("The lower bound should be less than"
                + "or equal to the upper boung");
        do
        {
            System.out.print("Enter the minimum value for the range: ");
            lower = in.nextInt();
            System.out.print("Enter the maximum value for the range: ");
            upper = in.nextInt();
            String skip = in.nextLine(); // skip remaining characters on the line

        } while (lower > upper);
        RangeInput rangeInput = new RangeInput(lower, upper);
        String command;
        System.out.println("Current value is " + rangeInput.getCurrent());
        System.out.println("Enter command [u=up, d=down, q=quit]");
        command = in.nextLine();
        while (!command.equalsIgnoreCase("q"))
        {
            if (command.equalsIgnoreCase("u"))
            {
                rangeInput.up();
            } else if (command.equalsIgnoreCase("d"))
            {
                rangeInput.down();
            } else
            {
                System.err.println("Your input must be u or d or q");
            }
            System.out.println("Current value is " + rangeInput.getCurrent());
            command = in.nextLine();
        }
        System.out.println("Done!");
    }

}
