import java.awt.Color;
import java.awt.Graphics;
import java.awt.Graphics2D;
import java.awt.Rectangle;

import javax.swing.JComponent;
import javax.swing.JFrame;

public class TwoSquareViewer
{
   public static void main(String[] args)
   {
      // Initialize Frame
      JFrame window = new JFrame();

      // Start Frame
      window.setSize(400, 300);
      window.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

      // Draw Component
      window.add(new TwoSquareComponent());

      window.setVisible(true);
   }
}

class TwoSquareComponent extends JComponent
{
   public void paint(Graphics g)
   {
      Graphics2D g2 = (Graphics2D) g;

      Rectangle box1 = new Rectangle(25, 25, 100, 100);
      g2.draw(box1);

      Rectangle box2 = new Rectangle(50, 50, 50, 50);
      g2.draw(box2);
   }
}
