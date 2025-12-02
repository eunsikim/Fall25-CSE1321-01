import java.util.Scanner;

public class Methods1{
    public static int calculate(int n1, int n2){
        int operation = n1 + n2;

        return operation;
    }

    public static void printMenu(){
        System.out.println("1 -> To do addition");
        System.out.println("2 -> To do subtraction");
        System.out.println("3 -> To do multiplication");
        System.out.println("4 -> To do division");
        System.out.println("0 -> To exit");
        System.out.print("> ");
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        while(true){
            printMenu();
            int selection = sc.nextInt();

            if(selection == 1){
                System.out.print("Enter a number: ");
                int number1 = sc.nextInt();
                
                System.out.print("Enter another number: ");
                int number2 = sc.nextInt();
                
                int result = calculate(number1, number2);

                System.out.println(number1 + " + " + number2 + " = " + result);
            }
            else if(selection == 0){
                System.out.println("Terminating Program...");
                break;
            }
            
        }

    }
}