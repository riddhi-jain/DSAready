/*Given a string S, check if it is palindrome or not. Print 1 if yes else print 0.

Approach:
use two pointers, initiating one from index 0 and other from last.
compare the elements at these pointers to be equal while start < end.
If successfully traversed, return 1
else 0. */


#include <bits/stdc++.h>
using namespace std;

class Solution{
public:	
	int isPlaindrome(string S)
	{
	    // Your code goes here
	    int start = 0;
	    int end = S.size()-1;
	    while(start < end){
	        if(S[start] != S[end]){
	            return 0;
	        }
	        start++;
	        end--;
	    }
	    return 1;
	}

};

// { Driver Code Starts.
int main() 
{
   	ios_base::sync_with_stdio(0);
    cin.tie(NULL);
    cout.tie(NULL);
   
   	int t;
   	cin >> t;
   	while(t--)
   	{
   		string s;
   		cin >> s;

   	    Solution ob;

   		cout << ob.isPlaindrome(s) << "\n";
   	}

    return 0;
}  // } Driver Code Ends
