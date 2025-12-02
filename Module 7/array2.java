public class array2 {
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

        int[] myNumbers2 = new int[10];
        myNumbers2[0] = 10;
        myNumbers2[1] = 20;

        for(int i = 2; i < myNumbers2.length; i++){
            myNumbers2[i] = i;
        }

        // How to update values in arrays
        myNumbers[4] = 40;
        myNumbers2[4] = 40;

        for(int i = 0; i < myNumbers.length; i++){
            if(myNumbers[i] != myNumbers2[i]){
                System.out.println("They are not the same");
                break;
            }

            if(i == myNumbers.length - 1){
                System.out.println("They are the same");
            }
        }


        // Search if myNumbers contains the value of 40
        int searchValue = 41;
        for(int i : myNumbers){
            if(i == searchValue){
                System.out.println("The array \"myNumbers\" contains the value of 40");
                break;
            }
        }
    }
}
