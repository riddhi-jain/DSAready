/*Given an array arr[] of size n and an element k. The task is to find the number of elements in array that appear more than X times(X = n/k).
Approach:
Create a hashmap and check for the value of each key in the map to be greater than n/k */

#include <iostream>
#include <bits/stdc++.h>
using namespace std;

class Solution
{
    public:
    map<int, int> m;
    //Function to find all elements in array that appear more than n/k times.
    int countOccurence(int arr[], int n, int k) {
        int x = n/k;
        int i;
        int count =0;
        for(i = 0; i< n; i++){
            m[arr[i]]++;
        }
        for(auto i : m){
            if(i.second > x){
                count++;
            }
            else{
                continue;
            }
        }
        return count;
    }
};


// { Driver Code Starts.
int main() {
    int t, k;
    cin >> t;
    while (t--) {
        int n, i;
        cin >> n;

        int arr[n];

        for (i = 0; i < n; i++) cin >> arr[i];
        cin >> k;
        Solution obj;
        cout << obj.countOccurence(arr, n, k) << endl;
    }
    return 0;
}
  // } Driver Code Ends
