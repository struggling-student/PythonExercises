public class CircuitTester {

    public static void main(String[] args) {
        
        Circuit wiring = new Circuit();
        
        wiring.toggleFirstSwitch();
	wiring.toggleFirstSwitch();
	wiring.toggleSecondSwitch();

        System.out.println("Switch 1: " + wiring.getFirstSwitchState());
        System.out.println("Expected: 0");
        System.out.println("Switch 2: " + wiring.getSecondSwitchState());
        System.out.println("Expected: 1");
        System.out.println("Lamp: " + wiring.getLampState());
        System.out.println("Expected: 1");
        
        wiring.toggleSecondSwitch();
        System.out.println("Switch 1: " + wiring.getFirstSwitchState());
        System.out.println("Expected: 0");
        System.out.println("Switch 2: " + wiring.getSecondSwitchState());
        System.out.println("Expected: 0");
        System.out.println("Lamp: " + wiring.getLampState());
        System.out.println("Expected: 0");
            
    }
}
