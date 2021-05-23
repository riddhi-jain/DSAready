//
//  main.cpp
//  Recover Binary Search Tree
//  Problem Statement

//  Two elements of a binary search tree (BST) are swapped by mistake.
//  Tell us the 2 values swapping which the tree will be restored.

//  Created by Giriraj Saigal on 23/05/21.
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

//  Definition for binary tree
struct TreeNode {
  int val;
  TreeNode *left;
  TreeNode *right;
  TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};

TreeNode* create(vector<int> x) {
    queue<TreeNode*> q;
    TreeNode* root = new TreeNode(x[0]);
    q.push(root);
    int i = 1;
    
    while(q.size() != 0) {
        int left = x[i++];
        int right = x[i++];
        TreeNode* t = q.front();
        q.pop();
        
        if(left != -1){
            t->left = new TreeNode(left);
            q.push(t->left);
        }
        
        if(right != -1){
            t->right = new TreeNode(right);
            q.push(t->right);
        }
    }
    
    return root;
}
 
bool isSorted(vector<int> x, int i, int j) {
    int temp = x[i];
    x[i] = x[j];
    x[j] = temp;
    
    for(int k = 0; k < 3; k++) {
        if(x[k] > x[k+1])
            return false;
    }
    
    return true;
}
vector<int> recoverTree(TreeNode* A) {
    vector<int> ans;
    stack<TreeNode*> st;
    TreeNode* temp = A;
    vector<int> vec;
    int prev = -1;
    int prevv = -1;
    
    while(st.size() > 0 || temp != NULL) {
        if(temp != NULL) {
            st.push(temp);
            temp = temp->left;
        }else{
            temp = st.top();
            st.pop();
            
            if(prev != -1){
                if(temp->val < prev) {
                    ans.push_back(prev);
                    ans.push_back(temp->val);
                }
            }
            vec.push_back(temp->val);
            prev = temp->val;
            temp = temp->right;
        }
    }
    
    if(ans.size() == 2){
        return {ans[1], ans[0]};
    }
    
    if(isSorted(ans, 0, 2))
        return {ans[2], ans[0]};
    if(isSorted(ans, 1, 2))
            return {ans[2], ans[1]};
    if(isSorted(ans, 0, 3))
            return {ans[3], ans[0]};
    if(isSorted(ans, 1, 3))
            return {ans[3], ans[1]};
            
    return {-1};
}


int main(int argc, const char * argv[]) {
    TreeNode* x = create({92,82,85,81,83,-1,88,70,-1,-1,-1,86,91,69,78,-1,87,89,84,-1,-1,76,80,-1,-1,-1,90,-1,96,75,77,79,-1,-1,-1,95,-1,74,-1,-1,-1,-1,-1,93,-1,72,-1,-1,94,71,73,-1,-1,-1,-1,-1,-1});
    recoverTree(x);
    return 0;
}
