/**
   This program demonstrates the Product class.
*/
public class ProductPrinter
{  
   public static void main(String[] args)
   {  
      Product product1 = new Product("Toaster", 29.95);
      Product product2 = new Product("Microwave", 124.95);

      System.out.print("product1 name: ");
      System.out.println(product1.getName());
      System.out.print("product1 price: ");
      System.out.println(product1.getPrice());

      System.out.print("product2 name: ");
      System.out.println(product2.getName());
      System.out.print("product2 price: ");
      System.out.println(product2.getPrice());

      product1.reducePrice(5);
      product2.reducePrice(5);

      System.out.print("product1 price: ");
      System.out.println(product1.getPrice());

      System.out.print("product2 price: ");
      System.out.println(product2.getPrice());
   }
}
