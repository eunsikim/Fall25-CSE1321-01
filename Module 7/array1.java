public class array1 {
    public static void main(String[] args) {
        // Initializing an Array of integers that can hold up to 3 int values
        // int[] myNumbers = {10, 20, 30};

        // Initializing an array of integers that can hold up to 10 int values
        int[] myNumbers = new int[10]; 

        myNumbers[0] = 10;
        myNumbers[1] = 20;

        for(int i = 2; i < myNumbers.length; i++){
            myNumbers[i] = i;
        }

        // This prints the object, not the contents of the array.
        System.out.println(myNumbers);

        // Instead, we have to go through each value one by one.
        for(int i : myNumbers){
            System.out.println(i);
        }
    }
}
