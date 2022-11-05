// SAMPLE
public class DoubleSizePicture
{
   public static void main(String[] args)
   {
      // Construct a blank picture and load image
      Picture pic = new Picture();
      pic.load("dog.jpg");

      // We want to show the middle portion of the *original*
      // picture, so shift the picture left and up to clip off
      // the left and top quarter of the original
      int dX = pic.getWidth() / 4;
      int dY = pic.getHeight() / 4;
      pic.move(-dX, -dY);
      
      // Now, scale the picture to double size. The result
      // is that the original central section of the image
      // now occupies the entire picture (magnified x 2)
      int doubleWidth = pic.getWidth() * 2;
      int doubleHeight = pic.getHeight() * 2;
      pic.scale(doubleWidth, doubleHeight);
   }
}
