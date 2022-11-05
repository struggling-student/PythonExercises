import javax.swing.*;

public class TwoSquareViewer
{
   public static void main(String[] args)
   {
      JFrame frame = new JFrame();

      frame.setSize(300, 400);
      frame.setTitle("TwoSquareViewer");
      frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

      TwoSquareComponent component = new TwoSquareComponent();
      frame.add(component);

      frame.setVisible(true);
   }
}
