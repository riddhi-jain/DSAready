'''
Given the root of a binary tree, return the same tree where every subtree (of the given tree) not containing a 1 has been removed.
A subtree of a node node is node plus every node that is a descendant of node.

Example:
               1                                  1
                 \                                 \
                  0          --------->             0
                /   \                                \
               0     1                                1


Input: root = [1,null,0,0,1]
Output: [1,null,0,null,1]
Explanation: 
The left child of right child of root satisfies the property "every subtree not containing a 1".
Hence, removed.

Approach:
1. The solution follows a recursive approach.
2. We keep on checking for both left and right subtree at each subtree.
3. If at any point we recieve a leaf node with value '0', we remove it from the tree by simply allocating the value null.
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pruneTree(self, root: TreeNode) -> TreeNode:
        # base case
        if root == None:
            return None
        
        root.left = self.pruneTree(root.left)
        root.right = self.pruneTree(root.right)
        
        if (root.val == 0 and root.left == None and root.right == None):
            return None
            
        return root
