/** This class models the circuit for a hallway light.
 */
public class Circuit {
    
    private int firstSwitch;    // 0 = down, 1 = up
    private int secondSwitch;
    private int lampState;      // 0 = on, 1 = off
    
    /** Gets the current state of the first switch
     * @return the state of the first switch (0 = down, 1 = up)
     */
    public int getFirstSwitchState()
    {
        return firstSwitch;
    }
    
    /** Gets the current state of the second switch
     * @return the state of the second switch (0 = down, 1 = up)
     */
    public int getSecondSwitchState()
    {
        return secondSwitch;
    }
    
    /** Gets the current state of the hallway lamp.
     * @return the state of the lamp (0 = off, 1 = on)
     */
    public int getLampState()
    {
        return lampState;
    }
    
    /** Changes the first switch from up to down, or vice versa.
     *  Toggling the switch also changes the state of the lamp.
     */
    public void toggleFirstSwitch()
    {
        firstSwitch = (firstSwitch + 1) % 2;
        lampState = (lampState + 1) % 2;
    }
    
    /** Changes the second switch from up to down, or vice versa.
     *  Toggling the switch also changes the state of the lamp.
     */
    public void toggleSecondSwitch()
    {
        secondSwitch = (secondSwitch + 1) % 2;
        lampState = (lampState + 1) % 2;
    }
}
