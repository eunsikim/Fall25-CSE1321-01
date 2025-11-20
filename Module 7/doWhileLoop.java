import java.util.Scanner;

public class doWhileLoop {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        boolean loop = true;

        do{
            System.out.println("1. Print Hello World");
            System.out.println("2. Exit");

            char choice = sc.nextLine().charAt(0);

            if(choice == '1'){
                System.out.println("Hello World");
            }
            else if(choice == '2'){
                System.out.println("Shutting off...");
                loop = false;
            }
            else{
                System.out.println("Error");
            }
        }
        while(loop == true);
    }
}
