/**
 * Rappresentazione di una lampadina.
 */
public class Lampadina {
    public int stato = 0; // 0 spenta, 1 accesa, -1 rotta.
    public int statoCorrente = 0; // 0 = no corrente, 1 corrente.
    public int numeroClickMassimo = 0;
    public int numeroClickAttuale = 0;

    public Lampadina(int numeroMaxClick)
    {
        stato = 0;
        numeroClickMassimo = numeroMaxClick;
        numeroClickAttuale = 0;
    }

    /**
     * Simula il cambio di stato nella lampadina se vi è corrente.
     */
    public void click(int nuovoStatoCorrente)
    {
        statoCorrente = nuovoStatoCorrente;

        if(statoCorrente == 1 && stato != -1)
        {
            stato = (stato + 1) % 2;
            numeroClickAttuale++;

            if(numeroClickAttuale > numeroClickMassimo)
            {
                stato = -1;
            }
        }
    }

    /**
     * Ottiene informazioni sullo stato della lampadina.
     * @return una stringa che rappresenta lo stato della lampadina.
     */
    public String stato()
    {
        if(stato == 0)
        {
            return "Stato Lampadina: Spenta.";
        }
        if(stato == 1)
        {
            return "Stato Lampadina: Accesa.";
        }
        else
        {
            return "Stato Lampadina: Rotta.";
        }
    }

    /**
     * Ottiene lo stato attuale della corrente.
     * @return una stringa che rappresenta lo stato della corrente.
     */
    public String statoCorrente()
    {
        if(statoCorrente == 0)
        {
            return "Non c'è corrente.";
        }
        else
        {
            return "Corrente in circolo.";
        }
    }
}
