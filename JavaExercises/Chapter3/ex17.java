/** 
 * Rappresenta un rettangolo con la sua base, altezza e fornisce
 * due metodi per il calcolo dell'area e del perimetro.
 */
public class Rettangolo
{
    private double base;
    private double altezza;

    public Rettangolo(double b, double h)
    {
        base = b;
        altezza = h;
    }

    /**
     * Ridefinisce lo stato interno del rettangolo.
     * @param nuovaBase è la nuova base.
     * @param nuovaAltezza è la nuova altezza.
     */
    public void ridimensiona(double nuovaBase, double nuovaAltezza)
    {
        base = nuovaBase;
        altezza = nuovaAltezza;
    }

    /**
     * Calcola il perimetro del rettangolo.
     * @return il perimetro calcolato.
     */
    public double perimetro()
    {
        return base*2 + altezza*2;
    }

    /**
     * Computes l'area del rettangolo.
     * @return l'area calcolata..
     */
    public double area()
    {
        return base*altezza;
    }
    
    /**
     * Return la base del rettangolo.
     * @return la base.
     */
    public double getBase()
    {
        return base;
    }

     /**
     * Return l'altezza del rettangolo.
     * @return l'altezza.
     */
    public double getAltezza()
    {
        return altezza;
    }

}
