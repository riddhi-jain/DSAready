//
//  main.cpp
//  79. Word Search
//
//  Given an m x n grid of characters board and a string word, return true if word exists in the grid.
//
//  The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.

//  Created by Giriraj Saigal on 24/05/21.
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


bool find(int cur, int len, pair<int,int> p, string word, vector<vector<char>>& board, vector<vector<int>> &dp) {
    if(cur == len-1)
        return true;
    int n = dp.size();
    int m = dp[0].size();
    int x = p.first;
    int y = p.second;
    dp[x][y] = 1;
    
    vector<int> Xs = {1,-1,0,0};
    vector<int> Ys = {0,0,1,-1};
    
    for(int i = 0; i < 4; i++) {
        int X = x+Xs[i];
        int Y = y+Ys[i];
        
        if(X >= 0 && X < n && Y >= 0 && Y < m && dp[X][Y] == 0 &&
          board[X][Y] == word[cur+1]) {
            bool fi = find(cur+1, len, {X,Y}, word, board, dp);
            if(fi)
                return true;
        }
    }
    
    dp[x][y] = 0;
    return false;
}
bool exist(vector<vector<char>> board, string word) {
    int n = (int)word.size();
    vector<pair<int,int>> vec;
    int p = (int)board.size();
    int q = (int)board[0].size();
    
    for(int i = 0; i < p; i++) {
        for(int j = 0; j < q; j++) {
            if(board[i][j] == word[0]){
                vec.push_back({i,j});
            }
        }
    }
    
    vector<vector<int>> dp(p, vector<int>(q, 0));
    for(int i = 0; i < (int)vec.size(); i++) {
        pair<int,int> k = vec[i];
        vector<vector<int>> dp1 = dp;
        if(find(0, n, k, word, board, dp1))
            return true;
    }
    
    return false;
}


int main(int argc, const char * argv[]) {
    vector<vector<char>> x = {{'A','B','C','E'},{'S','F','E','S'},{'A','D','E','E'}};
    exist(x,"ABCESEEEFS");
    return 0;
}
