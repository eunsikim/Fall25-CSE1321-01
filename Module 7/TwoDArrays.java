public class TwoDArrays {
    public static void main(String[] args) {
        int[] numbers_1 = new int[10];
        int[][] numbers_2 = new int[3][5];

        int[][] numbers_3 = {{1, 2}, {3, 4}};

        int count = 1;

        for(int i = 0; i < numbers_2.length; i++){
            for(int j = 0; j < numbers_2[i].length; j++){
                numbers_2[i][j] = count;
                count++;
            }
        }

        for(int i = 0; i < numbers_2.length; i++){
            for(int j = 0; j < numbers_2[i].length; j++){
                System.out.print(numbers_2[i][j] + "|");
            }
            System.out.println();
        }
    }
}
