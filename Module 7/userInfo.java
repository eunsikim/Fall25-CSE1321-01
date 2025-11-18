import java.util.Scanner;

public class userInfo {
    public static void main(String[] args) {
        String name;
        int age;

        Scanner sc = new Scanner(System.in);

        System.out.print("Enter your name: ");
        name = sc.nextLine();

        System.out.print("Enter your age: ");
        age = sc.nextInt();

        System.out.println("Your name is " + name);
        System.out.println("Your age is " + age);

        double pi = 3.14;
    }
}
