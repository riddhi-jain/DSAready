/*Given an NxN matrix Mat. Sort all elements of the matrix.
Print the sorted matrix.*/

#include <bits/stdc++.h>
using namespace std;

class Solution {
  public:
    vector<vector<int>> sortedMatrix(int N, vector<vector<int>> Mat) {
        int temp[N*N];
        int k = 0;
        for(int i = 0; i< N; i++){
            for(int j = 0; j< N; j++){
                temp[k] = Mat[i][j];
                k++;
            }
        }
        sort(temp, temp + N*N);
        k = 0;
        for(int i = 0; i< N; i++){
            for(int j = 0; j< N; j++){
                Mat[i][j] = temp[k];
                k++;
            }
        }
        return Mat;
    }
};

// { Driver Code Starts.

int main() {
    int t;
    cin >> t;
    while (t--) {
        int N;
        cin >> N;
        vector<vector<int>> v(N, vector<int>(N));
        for (int i = 0; i < N; i++)
            for (int j = 0; j < N; j++) cin >> v[i][j];
        Solution ob;
        v = ob.sortedMatrix(N, v);
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) cout << v[i][j] << " ";
            cout << "\n";
        }
    }
}  // } Driver Code Ends
