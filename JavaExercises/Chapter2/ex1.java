// SAMPLE
public class StringReplaceDemo {
    public static void main(String[] args) {
        String state = "Mississippi";
        
        state = state.replace("i", "ii");
        System.out.println("Length of new string: " +
                state.length());
        
        state = state.replace("ss", "s");
        System.out.println("Length of new string: " +
                state.length());
    }
}
