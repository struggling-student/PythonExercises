// SAMPLE
public class HalfSizePicture
{
   public static void main(String[] args)
   {
      // Construct a blank picture and load image
      Picture pic = new Picture();
      pic.load("cat.jpg");

      // Scale to half size
      int halfHeight = pic.getHeight() / 2;
      int halfWidth = pic.getWidth() / 2;
      pic.scale(halfWidth, halfHeight);

      // Center picture
      int dY = pic.getHeight() / 4;
      int dX = pic.getWidth() / 4;
      pic.move(dX, dY);
   }
}
