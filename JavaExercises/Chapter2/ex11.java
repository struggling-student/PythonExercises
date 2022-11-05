import java.awt.Color;
import javax.swing.*;

/**
   This class demonstrates the brighter method 
	of the Color class and displays the color.
 */
public class BrighterDemo
{
   public static void main(String[] args)
   {
      JFrame frame = new JFrame();
      frame.setSize(200,200);
		
      Color c = new Color(50, 100, 150);
      Color brighterColor = c.brighter();
		
      frame.getContentPane().setBackground(brighterColor);
      frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
      frame.setVisible(true);
   }    
}
