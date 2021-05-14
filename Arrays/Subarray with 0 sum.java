/*Given an array of positive and negative numbers. Find if there is a subarray (of size at-least one) with 0 sum.*/
import java.util.*;
import java.lang.*;
import java.io.*;

class GFG {
	public static void main (String[] args) {
		Scanner scan = new Scanner(System.in);
		//taking total number of testcases
		int t = scan.nextInt();
		while(t>0)
		{
		    //taking total count of elements
		    int n = scan.nextInt() ;
		    //Declaring and Initializing an array of size n
		    int arr[] = new int[n];
		    //adding elements to the array
		    for(int i = 0; i<n;i++)
		    {
		        arr[i] = scan.nextInt();
		    }
		    t--;
		     //calling the method findSum
		     //and print "YES" or "NO" based on the result
		     System.out.println(new Solution().findsum(arr,n)==true?"Yes":"No");
		}
	}
}

class Solution{
    //Function to check whether there is a subarray present with 0-sum or not.
    static boolean findsum(int arr[],int n)
    {
        Set<Integer> hs = new HashSet<Integer>();
        int sum = 0;
        for(int i = 0; i< n; i++){
            sum+=arr[i];
            if(arr[i] == 0 || sum == 0 || hs.contains(sum)){
                return true;
            }
            hs.add(sum);
        }
        return false;
    }
}
