public class whileLoop {
    public static void main(String[] args) {
        int x = 10;

        while(x >= 5 && x <= 20){
            System.out.println("x => " + x);
            x++; // Same to `x += 1` in python
        }
    }
}
