/*Given three arrays sorted in increasing order. Find the elements that are common in all three arrays.
Note: can you take care of the duplicates without using any additional Data Structure?*/


#include <bits/stdc++.h>
using namespace std;

class Solution
{
    public:    
       vector <int> commonElements (int A[], int B[], int C[], int n1, int n2, int n3)
        {
            int i = 0, j= 0, k= 0;
            int p1, p2,p3;
            p1 = p2 = p3 = INT_MIN;
            vector <int> answer;
            while(i < n1 && j < n2 && k < n3){
                while(A[i] == p1 && i < n1){
                    i++;}
                while(B[j] == p2 && j < n2 ){
                    j++;}
                while(C[k] == p3 && k < n3){
                    k++;}
                if(A[i] == B[j] && B[j] == C[k]){
                    answer.push_back(A[i]);
                    p1 = A[i]; p2 = B[j]; p3 = C[k];
                    i++; j++; k++;}
                else if( A[i] < B[j]){
                    p1 = A[i];
                    i++;}
                else if( B[j] < C[k]){
                    p2 = B[j];
                    j++;}
                else{
                    p3 = C[k];
                    k++;}
            }
            return answer;
        }
};
int main ()
{
    int t; cin >> t;
    while (t--)
    {
        int n1, n2, n3; 
        cin >> n1 >> n2 >> n3;
        int A[n1];
        int B[n2];
        int C[n3];
        
        for (int i = 0; i < n1; i++) cin >> A[i];
        for (int i = 0; i < n2; i++) cin >> B[i];
        for (int i = 0; i < n3; i++) cin >> C[i];
        
        Solution ob;
        
        vector <int> res = ob.commonElements (A, B, C, n1, n2, n3);
        if (res.size () == 0) 
            cout << -1;
        for (int i = 0; i < res.size (); i++) 
            cout << res[i] << " "; 
        cout << endl;
    }
} 
