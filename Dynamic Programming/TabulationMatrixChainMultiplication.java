// Problem Statement -- 
// Find the minimum number of multiplications needed to mulitply a sequence of matrices
// logic : This is a dynamic programming problem last time we applied memoisation
// which had a time compexity of O(N^3) and followed the recurssion approach
// Tabulation also has same time complexity but uses iteration instead of recurssion 
// So much more efficient

package DynamicProgramming;


public class TabulationMatrixChainMultiplication {

    // Here p takes the dimensions of the matrices 
    // Example : A1 = 1X2, A2 = 2X3, A3 = 3X9, then p = [1,2,3,9]
    // matrix Ai has dimension p[i-1] x p[i] for i = 1....n

    static int TabulationChainOrderSolution(int p[], int n) {

        int dp[][] = new int[n][n];
        int i, j, k, l, q;

        // the formula
        //dp[i,j] or dp[i][j] = minimum number of computations needed to compute the matrix(A[i,j]) where 
        // dimensions of A[i] = p[i-1]p[i]

        // For identical i and j
        // cost is 0 when multiplyting 1 matrix
        for( i=1 ; i<n; i++) {
            dp[i][i] = 0;
        }
        // l here is the matrix dimesnion presently being multiplied
        // We start with l = 2 since our two dimensions cannot have the same
        // value in any iteration of operation. So our values remain unique
        for(l = 2;  l<n; l++) {
            for( i=1; i<n-l+1; i++) {
                j = i + l - 1; // We define a variable to store the value for the 2nd value of the matrix
                // so the matrix becomes dp[i][j]
                if (j==n)
                    continue;
                dp[i][j] = Integer.MAX_VALUE;

                for( k=i; k <= j-1; k++) {
                    // q = scalar muliplications or cost

                    q = dp[i][k] + dp[k+1][j] + p[i-1]*p[k]*p[j];
                    if (q< dp[i][j]) 
                        dp[i][j] = q;
                }
            }
        }
        return dp[1][n-1]; // We are returning the value we tabulated 
        // In the table for the given length of the sequence of matrices
        // NOTE : THE 2D ARRAY IS NOT CONSIDERED TO BE THE MATRICES WE ARE OPERATING ON
        // BUT THE DYNAMIC PROGRAMMING CONCEPT OF TABULATION BEING IMPLEMENTED
        // ALSO WE ARE ONLY OPERATING ON THE DIMENSIONS OF THe CHAIN OF MATRICES
        // NOT THE ACTUAL MATRICES THEMSELVES
        // THE GOAL IS TO FIND OUT THE MINIMUM MULTIPLICATIONS NOT THE RESULT OF MULTIPLICATION
    }
    public static void main(String[] args) {
        int arr[] = new int[] { 1,2,3,4}; // {1,2,3,4} => 1X2 2x3 3x4 So there are 3 matrices
        int size = arr.length;
        System.out.println("Minimum number of multiplications : " + TabulationChainOrderSolution(arr,size));
    }
}
