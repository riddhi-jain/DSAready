/*Given an array of positive integers. Find the length of the longest sub-sequence such that elements in the subsequence are consecutive integers, the consecutive numbers can be in any order.
Approach:
Create a hashmap for the array.
Iterate though the array and check if arr[i]+1 exist as key in hashmap.
If yes, increment curr_max_length.
update max_length when a greater value is recieved.*/

// { Driver Code Starts
#include <bits/stdc++.h>
using namespace std;


 // } Driver Code Ends
class Solution{
  public:
    map<int,int> m;
    int findLongestConseqSubseq(int arr[], int N)
    {
        for(int i = 0; i<N; i++){
            m[arr[i]]++;
        }
        int max_length = 0;
        int curr_length = 0;
        sort(arr, arr+N);
        for(int i =0; i< N; i++){
            if(m.find(arr[i]+1) != m.end()){
                curr_length++;
                i+= (m[arr[i]]-1);
            }
            else{
                if(curr_length > max_length){
                    max_length = curr_length;
                }
                curr_length = 0;
            }
        }
        return (max_length+1);
    }
};

// { Driver Code Starts.
 
// Driver program
int main()
{
 int  t,n,i,a[100001];
 cin>>t;
 while(t--)
 {
  cin>>n;
  for(i=0;i<n;i++)
  cin>>a[i];
  Solution obj;
  cout<<obj.findLongestConseqSubseq(a, n)<<endl;
 }
      
    return 0;
}  // } Driver Code Ends
