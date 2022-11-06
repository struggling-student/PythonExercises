/**
 * Al momento non ci concentreremo sull'iteratività descritta
 * dalla consegna. Simuleremo un caso d'uso dato dalla sequenza
 * del metodo click().
 */

public class TestLampadina{
    public static void main(String[] args) {
        Lampadina l = new Lampadina(3);
        System.out.println(l.stato());
        l.click();
        System.out.println(l.stato());
        l.click();
        System.out.println(l.stato());
        l.click();
        System.out.println(l.stato());
        l.click();
        System.out.println(l.stato());
    }
