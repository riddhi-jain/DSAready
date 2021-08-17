/*Given an array arr of size n and an integer X. Find if there's a triplet in the array which sums up to the given integer X.
Algorithm : 

Sort the given array.
Loop over the array and fix the first element of the possible triplet, arr[i].
Then fix two pointers, one at i + 1 and the other at n – 1. And look at the sum, 
If the sum is smaller than the required number, increment the first pointer.
Else, If the sum is bigger, decrease the end pointer to reduce the sum.
Else, if the sum of elements at two-pointer is equal to given number return true.*/


#include <bits/stdc++.h>
using namespace std;

class Solution{
    public:
    bool find3Numbers(int A[], int arr_size, int sum)
    {
        int second_number, third_number;
        sort(A, A + arr_size);
        for (int i = 0; i < arr_size - 2; i++) {
            second_number = i+1;
            third_number = arr_size - 1;
            while(second_number < third_number ){
                if(A[i] + A[second_number] + A[third_number] == sum)
                    return true;
                else if(A[i] + A[second_number] + A[third_number] < sum)
                    second_number++;
                else
                    third_number--;
            }
        }
        return false;
    }
};

int main()
{
	int T;
	cin>>T;
	while(T--)
	{
		int n,X;
		cin>>n>>X;
		int i,A[n];
		for(i=0;i<n;i++)
			cin>>A[i];
		Solution ob;
        cout <<  ob.find3Numbers(A, n, X) << endl;
    }
}
