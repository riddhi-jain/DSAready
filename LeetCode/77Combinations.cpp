//
// Problem Statement
// Given two integers n and k, return all possible combinations of k numbers out of the range [1, n].
// You may return the answer in any order.
//
// Leetcode Problem: 77. Combinations
// Created by Giriraj Saigal on 22/05/21.
//

#include <iostream>
#include <cmath>
#include <vector>
#include <map>
#include <unordered_map>
#include <stack>
#include <queue>
#include <set>
using namespace std;



void solve(vector<int> inp, int n, int x, vector<vector<int>> &ans, int k) {
       if((int)inp.size() == k)
       {
           ans.push_back(inp);
           return;
       }
       
       for(int i = x; i <= n; i++) {
           inp.push_back(i);
           solve(inp, n, i+1, ans, k);
           inp.pop_back();
       }
       
   }
    vector<vector<int>> combine(int n, int k) {
        vector<int> vec;
        for(int i = 1; i <= n; i++)
            vec.push_back(i);
        vector<vector<int>> ans;
        solve({},n, 1, ans, k);
        return ans;
    }



int main(int argc, const char * argv[]) {
    vector<vector<int>> x = combine(4,2);
    return 0;
}
