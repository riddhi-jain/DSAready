/*Given a matrix of size r*c. Traverse the matrix in spiral form.

Approach: The problem can be solved by dividing the matrix into loops or squares or boundaries. It can be seen that the elements of the outer loop are printed first in a clockwise manner then the elements of the inner loop is printed. So printing the elements of a loop can be solved using four loops which prints all the elements. Every 'for' loop defines a single direction movement along with the matrix. The first for loop represents the movement from left to right, whereas the second crawl represents the movement from top to bottom, the third represents the movement from the right to left, and the fourth represents the movement from bottom to up.*/

// { Driver Code Starts
import java.io.*;
import java.util.*;
class GFG
{
    public static void main(String args[])throws IOException
    {
        Scanner sc = new Scanner(System.in);
        int t = sc.nextInt();
        
        while(t-- > 0)
        {
            int r = sc.nextInt();
            int c = sc.nextInt();
            
            int matrix[][] = new int[r][c];
            
            for(int i = 0; i < r; i++)
            {
                for(int j = 0; j < c; j++)
                 matrix[i][j] = sc.nextInt();
            }
            Solution ob = new Solution();
            ArrayList<Integer> ans = ob.spirallyTraverse(matrix, r, c);
            for (Integer val: ans) 
                System.out.print(val+" "); 
            System.out.println();
        }
    }
}// } Driver Code Ends

class Solution
{
    //Function to return a list of integers denoting spiral traversal of matrix.
    static ArrayList<Integer> spirallyTraverse(int matrix[][], int r, int c)
    {
        int k=0, l=0;
        int m = r;
        int n = c;
        ArrayList<Integer> ans = new ArrayList<Integer>();
        while( k < m && l < n){
            for(int i= l; i< n; ++i){
                ans.add(matrix[k][i]);}
            k++;
            for(int i = k; i<m;++i){
                ans.add(matrix[i][n-1]);}
            n--;
            if(k < m){
                for(int i = n-1; i >= l; --i){
                    ans.add(matrix[m-1][i]);
                }
                m--;
            }
            if(l < n){
                for(int i = m-1; i>=k; --i){
                    ans.add(matrix[i][l]);
                }
                l++;
            }
        }
        return ans;
    }
}
