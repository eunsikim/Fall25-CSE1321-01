public class forEachLoop {
    public static void main(String[] args) {
        String message = "Hello World";
        
        for(char x : message.toCharArray()){
            System.out.println(x);
        }
    }
}
