/* Given an array of integers, find the length of the longest (strictly) increasing subsequence from the given array.

Example:

Input:
N = 16
A[]={0,8,4,12,2,10,6,14,1,9,5,13,3,11,7,15}
Output: 6
Explanation:Longest increasing subsequence is 0 2 6 9 13 15, which has length 6.

Explaination :
The problem can be solved by recursion pr dynamic programming memoisation in O(n^2) time easily.
However a more efficient approach in O(nlogn) time is possible.
Highly recommend the article **https://www.geeksforgeeks.org/longest-monotonically-increasing-subsequence-size-n-log-n/** for best explaination.*/

// { Driver Code Starts

#include<bits/stdc++.h>
using namespace std;

 // } Driver Code Ends



class Solution
{
    public:
    
    int ceilIndex(int A[], int low, int high, int key)
    {
        while(low + 1< high){
            int mid = low + (high - low) / 2;
            if (A[mid] < key){
                low = mid;
            }
            else{
                high = mid;
            }
        }
        return high;
    }
    //Function to find length of longest increasing subsequence.
    int longestSubsequence(int n, int a[])
    {
       if (n == 0){
           return 0;
       }
       int tailTable[n];
       for (int i = 0; i< n; i++){
           tailTable[i] = 0;
       }
       int length = 1;
       tailTable[0] = a[0];
       for (int i = 1; i< n; i++){
           // case 1
           if (a[i] < tailTable[0]){
               tailTable[0] = a[i];
           }
           // case 2
           else if (a[i] > tailTable[length-1]){
               tailTable[length] = a[i];
               length++;
           }
           // case 3
           else{
               tailTable[ceilIndex(tailTable, -1, length - 1, a[i])] = a[i];
           }
       }
       return length;
    }
};

// { Driver Code Starts.
int main()
{
    //taking total testcases
    int t,n;
    cin>>t;
    while(t--)
    {
        //taking size of array
        cin>>n;
        int a[n];
        
        //inserting elements to the array
        for(int i=0;i<n;i++)
            cin>>a[i];
        Solution ob;
        //calling method longestSubsequence()
        cout << ob.longestSubsequence(n, a) << endl;
    }
}
  // } Driver Code Ends
