'''
Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”

Example:
Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
Output: 3
Explanation: The LCA of nodes 5 and 1 is 3.

Approach:
1. Start traversing the tree from the root node.
2. If the current node itself is one of p or q, we would mark a variable mid as True and continue the search for the other node in the left and right branches.
3. If either of the left or the right branch returns True, this means one of the two nodes was found below.
4. If at any point in the traversal, any two of the three: flags left, right or mid become True, this means we have found the lowest common ancestor for the nodes p and q.

Time complexity O(n) ans space complexity O(n)
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def recur(curr_node):
            if not curr_node: return False
            left = recur(curr_node.left)
            right = recur(curr_node.right)
            mid = (curr_node == p or curr_node == q)
            
            # if any two of left, right and mid become true, that means we got the LCA
            if left + right + mid >=  2:
                self.ans = curr_node
                
            # if any one of left, right, mid is true, that means we got either p or q or LCA
            return (mid or left or right)
            
        recur(root)
        return self.ans
        
