// Problem Statement --
// We are to determine the minimum number of multiplications required for a sequence of Matrices
// In matrix multiplication the computations may increase depending on the order we multiply the matrices in
// So we are to determine the most efficient order
// Category : Memoisation in Dynamic Programming
// Time complexity O(N^3)

package DynamicProgramming;
import java.util.Arrays;

public class MemoisationMatrixChainMultiplication 

{  
    // We assign the matrix we use for memoisation
    static int[][] dp = new int[100][100]; 

    // Here p takes the dimensions of the matrices 
    // Example : A1 = 1X2, A2 = 2X3, A3 = 3X9, then p = [1,2,3,9]
    // i is that starting 
    static int dpMatrixChainMemoised(int p[],int i,int j) 
    { 
        if(i==j) 
        {
            return 0; 
        }

        if (dp[i][j] != -1)  // If the given position is already filled. -1 refers to an empty position
        {
            return dp[i][j];
        }
        dp[i][j] = Integer.MAX_VALUE;
        for ( int k = i; k < j; k++)
         { 
            // We run the loop for the number of possible solutions we can get between i and j
            // Here we are applying the formula for minimum cost of multiplication 
            // Since we will be getting different values of i and j after each recurssion, we compare them all with each other to get the min value

            dp[i][j] = Math.min(dp[i][j], dpMatrixChainMemoised(p, i, k) + dpMatrixChainMemoised(p, k+1, j) + p[i-1]*p[k]*p[j]);
        }
        return dp[i][j];
    }
    
    // Here we define the function for returning  the 
    static int chainOrderMatrix(int [] p, int n) {
        int i = 1,j = n-1;  // i is simply the starting point 
        // Here we assign  as the last elements index in the matrix dimension array
        return dpMatrixChainMemoised(p, i, j);
    }
    // Driver Code
    public static void main(String[] args) 
    {
        int arr[] = { 1,2,3,4 }; // First we define the array with the dimensions for our sequence of matrices
        // {1,2,3,4} => 1X2 2x3 3x4 So there are 3 matrices
        int n = arr.length; // We get the length of the array i.e, for j = n-1
        
        for (int[] row : dp) {
            Arrays.fill(row, -1);
        }

        System.out.println(" The least number of multiplications required for the sequence of matrices " + chainOrderMatrix(arr, n));

    }
}

    

