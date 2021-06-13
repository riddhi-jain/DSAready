// Problem Statemement :
// Given a string and number of rows ‘n’. Print the string formed by concatenating n rows when input string is written in row-wise Zig-Zag fashion.
/* Examples: 
Input: str = "ABCDEFGH"
       n = 2
Output: "ACEGBDFH"
Explanation: Let us write input string in Zig-Zag fashion
             in 2 rows.
A   C   E   G   
  B   D   F   H
*/

package CodeWithScaler.Week2;

import java.util.Arrays;

public class ZigZagString 
{
    /* Approach 1 :
    Here we just assign a new String with the length of the number of rows 
    We use the boolean value down to determine if the element is at the last row or first
    */ 
    static void zigzag(int n, String A)
    {
        if(n==1 || n>=A.length())
        {
            System.out.println(A);
        }

        int row = 0;
        String[] arr = new String[n];

        // Example : for ABCDEFGH -> ACEG and BDFH so there are two rows here and the arr = ['ACEG','BDFH']
        
        Arrays.fill(arr,""); 
        boolean down=true;
        for(int i= 0; i<A.length(); i++)
        {
            arr[row] += A.charAt(i); 
            
            if (row==n-1) // We are at the last row
            {
                down = false;
            }
            else if(row==0) // We are the first row
            {
                down= true;
            }
            if(down) 
            {
                row++; // We increment when not in the last row
            }
            else
            {
                row--; // We decrement when in the last row
            }
        }
        for(int i=0; i<arr.length; i++)
        {
            System.out.println(arr[i]);
        }
    }

/*
Approach 2 : 
int numRows = 3
Example : 
"GEEKSFORGEEKS"
row = 0 = GSGS = 0, 4, 8, 12 = 0,+4,+4,+4
row = 1 = EKFREK = 2, 4, 6, 8 = 2, +2, +2, +2
row = 2 = EOE = 2, 6, 10 = 2, +4, +4
cycle = 2*3 - 2 = 4 -> 2*num_Rows - 2
middle_cycle = row + cycle - (2*row) 
*/
    static String zigzagoptimised(String s, int numRows)
    {
        if(numRows == 1 || numRows >= s.length())
        {
            return s;
        }
        int cycle = (2*numRows - 2);
        StringBuilder sb = new StringBuilder();
        for(int row=0; row<numRows; row++)
        {
            for( int j = row; j<s.length(); j+=cycle)
            {
                sb.append(s.charAt(j));
                int k  = j + cycle - (2*row);
                if(row!=0 && row!=numRows-1 && k<s.length())
                {
                    sb.append(s.charAt(k));
                }

            }

        }
        String result = sb.toString();
        return result;
         
        }
        public static void main(String[] args) {
            String s = "GEEKSFORGEEKS";
            int n = 3;
            System.out.println(zigzagoptimised(s,n));
            zigzag(n, s); 

        }

    }



