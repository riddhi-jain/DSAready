/*Given an array of integers (A[])  and a number x, find the smallest subarray with sum greater than the given value.

Note: The answer always exists. It is guaranteed that x doesn't exceed the summation of a[i] (from 1 to N).*/



#include <bits/stdc++.h>
using namespace std;

class Solution{
  public:

    int sb(int arr[], int n, int k)
    {
        int length = n;
        for(int i=0; i<n; i++){
            if(arr[i] > k){
                return 1;
            }
            int sum = arr[i];
            for(int j=i+1; j<n; j++){
                sum+= arr[j];
                if(sum > k){
                    int len = j - i + 1;
                    if(len < length){
                        length = len;
                    }
                    break;
                }
                else{
                    continue;
                }
            }
        }
        return length;
    }
};

// { Driver Code Starts.

int main() {
	int t;
	cin>>t;
	while(t--)
	{
		int n,x;
		cin>>n>>x;
		int a[n];
		for(int i=0;i<n;i++)
		cin>>a[i];
		Solution obj;
		cout<<obj.sb(a,n,x)<<endl;
	}
	return 0;
}  // } Driver Code Ends
