// Problem Statemement : 
// Implementing the depth first traversal problems using recurssion 
// Inorder -> Preorder -> Postorder 

// Time Complexity : O(N)

package Trees;
    // Let us firt define our node class
    class Node
    {
        int key; // We asign the key value for the parent node
        Node left, right; // We assign the left and right pointers for the child
        public Node (int data) 
        {
            key = data;
            left = right = null;
        }
    }
    class BinaryTree
    {
        // We initialise the root for the binary tree and set it to null for now
        Node root; 
        BinaryTree() // Constructor for the root 
        {
            root = null;
        }

        // In preOrder traversal we go from Root -> LeftChild -> RightChild
        void preOrder(Node node)
        {
            if(node == null)
            {
                return;
            }
            System.out.print(node.key + " " ); // First we print the root value
            preOrder(node.left); // Then we traverse the left subtree and print the root of it
            preOrder(node.right); // Similarly we traverse the right subtree and print the root of it
        }

        
        // In postOrder traversal we go from LeftChild -> RightChild -> Root
        void postOrder(Node node)
        {
            if(node==null)
            {
                return;
            }
            postOrder(node.left);
            postOrder(node.right);
            System.out.print(node.key + " ");
        }

        //  In inOrder traversal we go from leftChild -> Root -> RightChild
        void inOrder(Node node)
        {
            if(node==null)
            {
                return;
            }
            inOrder(node.left);
            System.out.print(node.key + " ");
            inOrder(node.right);
        }
        void preOrder() 
        {
            preOrder(root);
        }
        
        void postOrder() 
        {
            postOrder(root);
        }
        
        void inOrder() 
        {
            inOrder(root);
        }
        
        public static void main(String[] args) {
            BinaryTree tree = new BinaryTree();
            tree.root = new Node(1);
            tree.root.left = new Node(2);
            tree.root.right = new Node(3);
            tree.root.left.left = new Node(4);
            tree.root.left.right = new Node(5);

            System.out.print( "Preorder traversal of binary tree is : ");
            tree.preOrder();
            System.out.print( "\nPostorder traversal of binary tree is : ");
            tree.postOrder();
            System.out.print( "\nInorder traversal of binary tree is : ");
            tree.inOrder();    
            /*
            Preorder traversal of binary tree is : 1 2 4 5 3 
            Postorder traversal of binary tree is : 4 5 2 3 1
            Inorder traversal of binary tree is : 4 2 5 1 3
            */  
    }
}