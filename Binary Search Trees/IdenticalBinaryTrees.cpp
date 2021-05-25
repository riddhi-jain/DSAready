//
//  main.cpp
//  Identical Binary Trees
//
//  Given two binary trees, write a function to check if they are equal or not.
//
//  Two binary trees are considered equal if they are structurally identical and the nodes have the same value.
//
//  Return 0 / 1 ( 0 for false, 1 for true ) for this problem
//
//  Example :
//
//  Input :
//
//     1       1
//    / \     / \
//   2   3   2   3
//
//  Output :
//    1 or True
//  Created by Giriraj Saigal on 25/05/21.

#include <iostream>
#include <cmath>
#include <vector>
#include <map>
#include <unordered_map>
#include <stack>
#include <queue>
#include <set>
using namespace std;

 // Definition for binary tree
struct TreeNode {
  int val;
  TreeNode *left;
  TreeNode *right;
  TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};
 
int check(TreeNode* A, TreeNode* B) {
    if(A == NULL && B == NULL)
        return 1;
    
    if(A == NULL || B == NULL)
        return 0;
    
    if(A->val != B->val)
        return 0;
    
    int left = check(A->left, B->left);
    int right = check(A->right, B->right);
    
    return left & right;
}

int isSameTree(TreeNode* A, TreeNode* B) {
    return check(A,B);
}


int main(int argc, const char * argv[]) {
    // insert code here...
    std::cout << "Hello, World!\n";
    return 0;
}
