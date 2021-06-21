// Problem Statement : Implement the Iteratieve DFS approach for Preorder, Postorder and Inorder traversals for binary tree.
//Time complexity : O(N)

package Trees;
import java.util.Stack;

class TreeNode 
    {
        int key;
        TreeNode left,right;
        TreeNode(int data)
        {
            key = data;
            left = right = null;
        }
    }

class IterativeBinaryTree
    {   
        TreeNode root;

        // Implementing Iterative inorder 
        void IterativeInorder()
        {
            if (root==null) // First we check for the corner cases
            {
                return;
            }

            Stack<TreeNode> s = new Stack<TreeNode>(); // Then let us define a new stack
            TreeNode curr = root; // And initialise curr as root
            while(curr != null || s.size() >0 ) // As long as current is not null and the stack is not empty
            {
                while(curr!=null) 
                {
                    s.push(curr); // We push the current node into the stack
                    curr = curr.left; // And then we traverse the left subtree
                }
                curr = s.pop(); // After we have traversed all of the left subtree we pop each element ( which will always be a left subtree element and print them 
                System.out.print(curr.key + " ");
                curr = curr.right; // After printing the said left subtree element we check if that node had anything in it's right. If it does, in the next iteration we print 
                // THe right element and push it into the stack otherwise we return null.
            }
        }
        
        void postOrderIterative(TreeNode root) {
            Stack<TreeNode> stack = new Stack<>(); // We create a new stack
            while(true) {
                while(root != null) { // Whenever root is null we push our root into the stack twice
                    stack.push(root);
                    stack.push(root);
                    root = root.left; // And we do this for the entire left subtree
                }
                if(stack.empty()) return;
                root = stack.pop(); // We then set root as the top element of the stack
                
                if(!stack.empty() && stack.peek() == root) root = root.right; // If our stack is not empty and the top element of the stack is equal to th stack we traverse the right subtree
                 
                else {
                     
                    System.out.print(root.key + " "); root = null; // If right child is null then we print our element
                }
            }
        }
        void IterativePreOrder(TreeNode root)
        {
            // We first create a node stack and push the root into the stack
            Stack<TreeNode> nodeStack = new Stack<TreeNode>();
            nodeStack.push(root); // We first push in the root of the tree
            while(!nodeStack.isEmpty()) // Now as long as our stack is not empty
            {
                TreeNode myNode = nodeStack.pop(); // We create a new node and set it as the top element of the stack
                System.out.print(myNode.key + " "); // We then print the top element
                if(myNode.right!=null) // After printing we check for it's right child and push it in
                {
                    nodeStack.push(myNode.right); // We are pushing in the right child first because according to LIFO we need to process our left child first
                }
                if(myNode.left!=null)
                {
                    nodeStack.push(myNode.left); // We then push in our left child
                }
            }
        }
         
        public static void main(String[] args) {
            IterativeBinaryTree tree = new IterativeBinaryTree();
            tree.root = new TreeNode(1);
            tree.root.left = new TreeNode(2);
            tree.root.right = new TreeNode(3);
            tree.root.left.left = new TreeNode(4);
            tree.root.left.right = new TreeNode(5);
            System.out.print(" The Iterative Inorder traversal is : ");
            tree.IterativeInorder(); 
            
            System.out.print(" The Iterative postOrder traversal is : ");
            tree.postOrderIterative(tree.root);
            
            System.out.print(" The Iterative preOrder traversal is : ");

            tree.IterativePreOrder(tree.root);
        }
    }
/* Output : 
The Iterative Inorder traversal is : 4 2 5 1 3  The Iterative postOrder traversal is : 4 5 2 3 1  The Iterative preOrder traversal is : 1 2 4 5 3

*/
