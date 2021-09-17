'''
Given an n-ary tree, return the level order traversal of its nodes' values.

Nary-Tree input serialization is represented in their level order traversal, each group of children is separated by the null value (See examples).

Example:
          1
        / | \
       3  2  4
      / \
     5   6
Input: root = [1,null,3,2,4,null,5,6]
Output: [[1],[3,2,4],[5,6]]

Approach:
1. Consider an 'ans' array (to store final answer) and a 'level' array to store all the nodes at one level.
2. Run an iterative approach where we keep adding the values of all nodes at that level to answer array and children of each node is added to another array 'temp'.
3. The new 'level' array for next iteration is the 'temp' array.
'''


class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

class Solution(object):
     def levelOrder(self, root):
        """
        :type root: Node
        :rtype: List[List[int]]
        """
        if not root:
            return []
        ans = []
        level = [root]
        
        while(level):
            ans.append([node.val for node in level])
            
            temp = []
            for node in level:
                for child in node.children:
                    if child:
                        temp.append(child)
                        
            level = temp
        
        return ans
