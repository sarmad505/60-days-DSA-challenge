// ojective of program is that an array will be given
// and a target number will be given
// if two numbers in the array summed up are equal to that target
// give the index of those two numbers
// otherwise return 0;
public class App9 {
    public static void main(String[] args) {
        int[] nums = { 2, 7, 11, 15 };
        int target = 10;
        printArray(findNum(nums, target));

    }

    public static int[] findNum(int[] arr, int target) {
        int[] answerArray = { 0, 0 };
        for (int i = 0; i < arr.length; i++) {
            int myNum = target - arr[i];
            for (int j = 0; j < arr.length; j++) {
                if (myNum == arr[j]) {
                    answerArray[0] = j;
                    answerArray[1] = i;
                    break;
                }
            }
        }
        return answerArray;

    }

    public static void printArray(int[] arr) {
        for (int i = 0; i < arr.length; i++) {
            System.out.print(arr[i] + " ");
        }
    }
}