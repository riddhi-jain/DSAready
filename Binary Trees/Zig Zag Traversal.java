// Problem Statement: 
// Find the Zig-Zag level order traversal of a binary tree
// Time Complexity: O(N)
/*
Example: 
Input:
           7
        /     \
       9       7
     /  \     /   
    8    8   6     
   /  \
  10   9 
Output:
7 7 9 8 8 6 9 10 
*/
package Trees;

import java.util.LinkedList;
import java.util.Queue;

class ZigZagTree
{
    TreeNode root;

    void ZigZagTraversal()
    {
        if(root==null) return;
        Queue<TreeNode> q = new LinkedList<>();
        q.add(root);
        while(!q.isEmpty())
        {
            TreeNode temp = q.poll();

            System.out.print(temp.key + " ");

            if(temp.right!=null)
            {
                q.add(temp.right);
            }
            if(temp.left!=null)
            {
                q.add(temp.left);
            }
            
        }
        
    }
    public static void main(String args[])
    {
       ZigZagTree tree = new ZigZagTree();
       tree.root= new TreeNode(1);
       tree.root.left= new TreeNode(2);
       tree.root.right= new TreeNode(3);
       tree.root.left.left= new TreeNode(4);
       tree.root.left.right= new TreeNode(5);
        
       System.out.println("The Zig Zag level order traversal is: ");
       tree.ZigZagTraversal();
    }

}
/*
output:
The Zig Zag level order traversal is:   
1 3 2 5 4
*/