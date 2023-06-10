// Day1:TwoSum Problem

// Explain:-
// Given an array of unique integers and a target sum, the task is to find any
// two numbers from the array that add up to the target sum.
// Return the pair of numbers in an array if found, or null if no such pair exists
// or the input array is invalid (null or length less than two).

import java.util.*;

class Day1TwoSum {

  public static int[] twoSumFunc(int[] numbers, int targetSum) {
    if (numbers == null || numbers.length < 2) {
      return null;
    } else {
      for (int i = 0; i < numbers.length; i++) {
        int diff = targetSum - numbers[i];
        for (int j = i + 1; j < numbers.length; j++) {
          if (numbers[j] == diff) {
            return new int[] { numbers[i], numbers[j] };
          }
        }
      }
    }
    return null;
  }

  public static void main(String[] args) {
    System.out.println(
      Arrays.toString(twoSumFunc(new int[] { 3, 6, 10, 14 }, 17))
    );
  }
}
