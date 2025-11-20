import java.util.Scanner;

public class input1 {
    public static void main(String[] args) {
        String name;
        int age;
        String address;

        Scanner sc = new Scanner(System.in);

        System.out.print("Enter your name: ");
        name = sc.nextLine();

        System.out.print("Enter your age: ");
        age = Integer.parseInt(sc.nextLine());

        System.out.print("Enter you address: ");
        address = sc.nextLine();

        System.out.println("Your name is " + name);
        System.out.println("Your age is " + age);
        System.out.println("Your address is " + address);

        double pi = 3.14;
    }
}
