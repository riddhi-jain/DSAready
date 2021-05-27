package Stacks;


public class StackAsLinkedLists {           
    StackNode root;
    // So this is how you declare a Node in Java. Not what i expected but aight
    static class StackNode {
        int data;
        StackNode next;
        StackNode ( int data ) { this.data = data; }
    }
    public boolean isEmpty() 
    {
        if (root==null) {
            return true;
        }
        else {
            return false;
        }
    }
    public void push(int data) {
        StackNode newNode = new StackNode(data); // We create the new node with
        // the data required 

        if (root==null) {
            root = newNode;
        }
        else {
            StackNode temp = root; // first we make a new reference for the root node
            root = newNode; // Now we break the link and link the root to the newNode
            newNode.next = temp; // Next we create the link between the newNode and the head node by using
            // the address referenced in the root node 
        }
        System.out.println(data + " Pushed to the stack ");
    }
    public StackAsLinkedLists() {
        root = null;
    }
    public int pop() {
        int popped;
        if (root==null) {
            System.out.println("Stack is empty");
            return 0;
        }
        else {
            popped = root.data;
            root = root.next;
            return popped;
        }
       
    }
    public int peek() {
        if(root==null) {
            System.out.println("Stack is empty");
            return 0;
        }
        else { 
            return root.data;
        }

    }
    public static void main(String[] args) {
        StackAsLinkedLists s = new StackAsLinkedLists();
        s.push(10);
        s.push(20);
        s.push(100);
        s.push(300);
        System.out.println (s.pop() + " is the element that was popped");
        
    }
    
}
