public class TestRettangolo {
    
    public static void main(String[] args) {

        // Creazione dei rettangoli.
        Rettangolo r1 = new Rettangolo(5, 10);
        Rettangolo r2 = new Rettangolo(4, 2);;
        Rettangolo r3 = new Rettangolo(6, 12);

        // Somma aree.
        double sommaAree = r1.area() + r2.area() + r3.area();
        // Somma perimetri.
        double sommaPerimetri = r1.perimetro() + r2.perimetro() + r3.perimetro();
        // Stampa
        System.out.println("Somma aree: " + sommaAree);
        System.out.println("Somma perimetri: " + sommaPerimetri);

        // Ridimensionamento del primo rettangolo
        r1.ridimensiona(6, 2);
        // Stampa delle nuove misure.
        System.out.println("\nNuove dimensioni del primo rettangolo:\n");
        System.out.println("Base: " + r1.getBase());
        System.out.println("Altezza: " + r1.getAltezza());
    }
}
