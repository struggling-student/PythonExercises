/**
 * La seguente classe simula il comportamento di un interruttore.
 */
public class Interruttore {
    Lampadina lampadina;
    int statoCorrente = 0; // 0 = no corrente, 1 = corrente.
    
    public Interruttore(Lampadina lamp)
    {
        lampadina = lamp;
    }

    /**
     * Realizza il passaggio della corrente accendendo la 
     * corrispondente lampadina.
     */
    public void click()
    {
        statoCorrente = (statoCorrente + 1) % 2;
        lampadina.click();
    }
}
