/**
 * E2_3
 * Demonstrate the behavior of String's trim() function.
 * Additionally show how to use the replace() function from String
 * to remove all spaces from a string
 */

public class E2_3
{

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args)
    {
        System.out.println ("This program demonstrates the behavior of String's trim() function.\n");
        String data = "  Here is a string   with  multiple spaces   ";
        // Demonstrate the use of trim
        System.out.println("The starting string is ");
        System.out.println( data);
        System.out.println("And here it is after applying the trim function");
        System.out.println( data.trim() );
        System.out.println("And after removing all spaces using the replace function:");
        System.out.println(data.replace(" ",""));

    }

}
