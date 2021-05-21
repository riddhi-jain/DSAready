/*Given an array of n positive integers and a number k. Find the minimum number of swaps required to bring all the numbers less than or equal to k together.

Approach:
Using two-pointer technique and a sliding window to size of number of elements <= k*/


#include <iostream>
using namespace std;
int minSwap(int *arr, int n, int k);
// Driver code
int main() {

	int t,n,k;
	cin>>t;
	while(t--)
    {
        cin>>n;
        int arr[n];
        for(int i=0;i<n;i++)
            cin>>arr[i];
        cin>>k;
        cout << minSwap(arr, n, k) << "\n";
    }
	return 0;
}
// } Driver Code Ends


int minSwap(int *arr, int n, int k) {
    // variabble less to store numbers <= k
    int less=0;
    for(int i = 0; i< n; i++){
        if(arr[i] <= k){
            less++;
        }
    }
    // variable more to store numbers > k in first window
    int more=0;
    for(int i =0; i<less; i++){
        if(arr[i] > k)
            more++;
    }
    // variables final and j initiated 
    int final = more;
    int j = less;
    for(int i =0; i<n; i++){
        if(j == n){
            break;
        }
        if(arr[i] > k){
            more--;
        }
        if(arr[j] > k){
            more++;
        }
        final = min(final, more);
        j +=1;
    }
    return final;
}
