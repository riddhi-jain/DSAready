'''
Given the root of an n-ary tree, return the preorder traversal of its nodes' values.

Nary-Tree input serialization is represented in their level order traversal. Each group of children is separated by the null value (See examples)

Example:
          1
        / | \
       3  2  4
      / \
     5   6
		 
Input: root = [1,null,3,2,4,null,5,6]
Output: [1,3,5,6,2,4]

Approach:
The approach is similar to that of binary tree preorder traversal, the only difference being that for each parent node all the children (left -> right) need to be added to the traversal. This is accomplished by an iterative approach.
'''


class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

class Solution(object):
    def preorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        ans = []
        level = root and [root]
        
        while(level):
            curr = level.pop()
            ans.append(curr.val)
            level += [child for child in reversed(curr.children) if child]
            
        return ans
