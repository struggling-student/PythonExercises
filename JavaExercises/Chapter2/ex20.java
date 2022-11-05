import javax.swing.JComponent;
import java.awt.Color;
import java.awt.Graphics;
import java.awt.Graphics2D;
import java.awt.Rectangle;

/**
   Draws two solid squares: one in pink and one in purple. Use a standard color
   for one of them and a custom color for the other.
 */
public class TwoSquareComponent extends JComponent
{
   public void paintComponent(Graphics g)
   {
      Graphics2D g2 = (Graphics2D) g;

      int sidelength = 100;

      // draw a pink square
      Rectangle square1
         = new Rectangle(0, 0, sidelength, sidelength);
      g2.setColor(Color.pink);
      g2.fill(square1);

      // draw a custom colored purple square
      Rectangle square2
         = new Rectangle(0, sidelength, sidelength, sidelength);
      g2.setColor(new Color(0.7F, 0, 0.7F));
      g2.fill(square2);
   }
} 
