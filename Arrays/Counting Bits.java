/*
Given an integer n, return an array ans of length n + 1 such that for each i (0 <= i <= n), ans[i] is the number of
1's in the binary representation of i.

Example :

Input: n = 2
Output: [0,1,1]
Explanation:
0 --> 0
1 --> 1
2 --> 10

Approach: Using Integer.toBinaryString method to create the binary representation of i, counting the occurrences of 1's
with Stream API (available from Java 8)
 */

public class CountingBits {

    public static int[] countBits(int n) {
        int[] ans = new int[n + 1];

        for (int i = 0; i < ans.length; i++) {
            ans[i] = (int) Integer.toBinaryString(i)
                    .chars()
                    .filter(character -> character == '1')
                    .count();
        }

        return ans;
    }
}
