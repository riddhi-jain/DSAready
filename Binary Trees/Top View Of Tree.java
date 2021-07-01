/*
Problem Statement: Given a binary tree, print the top view of it. 
Example:
       1
    /     \
   2       3
  /  \    / \
 4    5  6   7
Top view of the above binary tree is
4 2 1 3 7

*/


package Trees;
import java.util.LinkedList;
import java.util.Map;
import java.util.Queue;
import java.util.TreeMap;
import java.util.Map.Entry;

class topViewTree
{
    TreeNode root;
    void TopViewTraversal()
    {   
        // Let us define the queueObj that we are gonna be using for
        // storing both our Line number (hd) and Node values for the respective hd.
        class QueueObj
        {
            TreeNode node;
            int hd;
            QueueObj(TreeNode node, int hd)
            {
                this.node = node;
                this.hd = hd;
            }
        }
        Queue<QueueObj> q = new LinkedList<>();
        Map<Integer, TreeNode> topViewMap = new TreeMap<Integer, TreeNode>();

        // Let us define our base condition
        if(root==null) return;
        else q.add(new QueueObj(root, 0)); // We add the first element into the queue
        while(!q.isEmpty())
        {
            QueueObj temp = q.poll(); // We get the headmost element in the queue
            
            if(!topViewMap.containsKey(temp.hd)) // If our tree map does not contain the line number from the queue object
            {
                // Only then we push it into our treemap
                // So no repeating elements can be availed in our map
                topViewMap.put(temp.hd, temp.node); 
            }
            if(temp.node.left!=null)
            {
                q.add(new QueueObj(temp.node.left, temp.hd-1));
            }
            if(temp.node.right!=null)
            {
                q.add(new QueueObj(temp.node.right, temp.hd+1));
            }
        }
        // Now we use the Entry class to iterate over our Map
        for(Entry<Integer, TreeNode> entry: topViewMap.entrySet())
        {
            System.out.println(entry.getValue().key);
        }

}
public static void main(String[] args)
    {
        /* Create following Binary Tree
            1
        / \
        2 3
        \
            4
            \
            5
            \
                6*/
        topViewTree tree = new topViewTree();
        tree.root = new TreeNode(1);
        tree.root.left = new TreeNode(2);
        tree.root.right = new TreeNode(3);
        tree.root.left.right = new TreeNode(4);
        tree.root.left.right.right = new TreeNode(5);
        tree.root.left.right.right.right = new TreeNode(6);
        System.out.println(
            "Following are nodes in top view of Binary Tree");
        tree.TopViewTraversal();
    }
}
/* 
Output: 
Following are nodes in 
top view of Binary Tree
2
1
3
6

*/