/** 
 * Anche in questo caso, l'iterazione verrà sostituita con una 
 * sequenza di chiamate al metodo click.
 */
public class TestInterruttore {
    public static void main(String[] args) {
        
        // Creazione della lampadina.
        Lampadina lamp = new Lampadina(2);

        // Creazione di due interruttori collegati alla stessa lampadina.
        Interruttore interruttore_1 = new Interruttore(lamp);
        Interruttore interruttore_2 = new Interruttore(lamp);

        // I due interruttori agiscono in alternanza sulla stessa lampadina,
        // mostrando come lo stato di quest'ultima cambi in modo coerente.
        interruttore_1.click();
        System.out.println(lamp.stato());
        System.out.println(lamp.statoCorrente());
        
        interruttore_2.click();
        System.out.println(lamp.stato());
        System.out.println(lamp.statoCorrente());
        
        interruttore_1.click();
        System.out.println(lamp.stato());
        System.out.println(lamp.statoCorrente());
        
        interruttore_2.click();
        System.out.println(lamp.stato());
        System.out.println(lamp.statoCorrente());
        
        interruttore_1.click();
        System.out.println(lamp.stato());
        System.out.println(lamp.statoCorrente());
    };
}
