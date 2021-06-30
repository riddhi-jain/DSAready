/*
Problem Statement: Get the boundary traversal of a binary tree
Example: 
Input:
          20
        /   \
       8     22
     /   \    \
    4    12    25
        /  \ 
       10   14 

Output: 20 8 4 10 14 25 22
*/
package Trees;


class BoundaryTree
{
  static TreeNode root;
  void printLeafNodes(TreeNode root)
  {
    if(root==null) return;
    if(root.left==null && root.right==null)
    {
      System.out.print(root.key + " ");
      return;
    }
    if(root.left!=null) printLeafNodes(root.left);
    if(root.right!=null) printLeafNodes(root.right);
    
  }
  void leftBoundary(TreeNode temp)
  {
    if(temp==null) return;
    if(temp.left!=null)
    {
      System.out.print(temp.key + " ");
      leftBoundary(temp.left);
    }
    else if(temp.right!=null)
    {
      System.out.println(temp.key);
      leftBoundary(temp.right);
    }
  }
  
void rightBoundary(TreeNode temp)
{
  if(temp==null) return;
  if(temp.right!=null)
  {
    rightBoundary(temp.right);
    System.out.print(temp.key + " ");
  }
  else if(temp.left!=null)
  {
    
    System.out.print(temp.key);
    rightBoundary(temp.left);
  }
}

void BoundaryTraversal(TreeNode root)
{
  System.out.println("The Boundary Traversal of the binary tree is: ");
  leftBoundary(root);
  printLeafNodes(root);
  rightBoundary(root.right); // So we do not print the root 
}
public static void main(String[] args) {
        BoundaryTree tree = new BoundaryTree();
        tree.root = new TreeNode(20);
        tree.root.left = new TreeNode(8);
        tree.root.left.left = new TreeNode(4);
        tree.root .left.right = new TreeNode(12);
        tree.root.left.right.left = new TreeNode(10);
        tree.root.left.right.right = new TreeNode(14);
        tree.root.right = new TreeNode(22);
        tree.root.right.right = new TreeNode(25);
        tree.BoundaryTraversal(root);
}
}
/*
The Boundary Traversal of the binary tree is: 
20 8 4 10 14 25 22 
*/