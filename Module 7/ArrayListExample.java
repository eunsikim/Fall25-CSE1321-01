import java.util.ArrayList;
import java.util.Scanner;

public class ArrayListExample {
    public static void main(String[] args) {
        ArrayList<String> names = new ArrayList<>();

        names.add("Eun Sik"); // names ["Eun Sik"]
        names.add(0, "John Doe"); // names ["John Doe", "Eun Sik"]


        for(int i = 0; i < names.size(); i++){
            System.out.println(names.get(i));
        }

        ArrayList<Integer> numbers_1 = new ArrayList<>();
        ArrayList<Short> numbers_2 = new ArrayList<>();
        ArrayList<Float> grades_1 = new ArrayList<>();
        ArrayList<Double> grades_2 = new ArrayList<>();


        Scanner sc = new Scanner(System.in);

        System.out.println("Enter a number: ");
        int newNumber = sc.nextInt();
        numbers_1.add(newNumber);

        for(int i = 0; i < 10; i++){
            numbers_1.add(i);
        }

        for(int i = 0; i < 10; i++){
            System.out.println(numbers_1.get(i));
        }
    }
}
