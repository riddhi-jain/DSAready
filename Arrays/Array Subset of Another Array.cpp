/*Given two arrays: a1[0..n-1] of size n and a2[0..m-1] of size m. Task is to check whether a2[] is a subset of a1[] or not. Both the arrays can be sorted or unsorted. It may be assumed that elements in both array are distinct.

Approach:
1.Create a hashmap for a1
2.For each element of a2 check if there exist a key equal to that element in the hashmap */


#include <bits/stdc++.h>
using namespace std;

string isSubset(int a1[], int a2[], int n, int m) ;

int main() {
    int t;
    cin >> t;

    while (t--) {
        int n, m;
        cin >> n >> m;
        int a1[n], a2[m];

        for (int i = 0; i < n; i++) {
            cin >> a1[i];
        }
        for (int i = 0; i < m; i++) {
            cin >> a2[i];
        }

        cout << isSubset(a1, a2, n, m) << endl;
    }
    return 0;
}

string isSubset(int a1[], int a2[], int n, int m) {
    map<int,int> mp;
    for(int i = 0; i< n; i++){
        mp[a1[i]]++;
    }
    string s1 = "No";
    string s2 = "Yes";
    
    for(int i=0; i<m; i++){
        if(mp.find(a2[i]) == mp.end()){
            return s1;
        }
    }
    return s2;
}
