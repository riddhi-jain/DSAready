// Problem Statement : To implement Queues with linked lists
// Time complexty : O(1)
package Queues;
// We first define a linked list node to define a queue entry
public class QueueWithLinkedLists 
{
    int data;
    QueueWithLinkedLists next;

    // We define our constructor to create a new linked list node
    public QueueWithLinkedLists(int data) {
        this.data = data;
        this.next = null;
    }
}

// This is the class we use to represent the queue
class Queue 
{
    QueueWithLinkedLists front, rear;

    public Queue() 
    {   
        // Here we define an empty queue since front and rear indices are set to none
        this.front = this.rear = null;
    }
    // Inorder to add elemenets to a queue at the rear
    void enqueue(int data) 
    {
        QueueWithLinkedLists temp = new QueueWithLinkedLists(data);
        // If our queue is empty
        if (this.rear == null ) 
        {
            this.front  = this.rear = temp;
            return;
        }
    
        this.rear.next = temp; // This sets our rear pointer to a new node temp
        this.rear = temp; // And then we asign temp as our new rear pointer
        System.out.println(data + " is Enqueued");
    }
    void dequeue() 
    {
        if(this.front == null) 
        {
            return;
        }
        // We store our front in a new node temp
        QueueWithLinkedLists temp = this.front;
        // Then we move our front pointer a node ahead
        // This will make the front pointer not point to the first node and point
        this.front = this.front.next;
        if( this.front == null) 
        {
            this.rear = null;
        }
    }



public static void main(String[] args) 
{
    Queue q = new Queue();
        q.enqueue(10);
        q.enqueue(20);
        q.dequeue();
        q.dequeue();
        q.enqueue(30);
        q.enqueue(40);
        q.enqueue(50);
        q.dequeue();
        System.out.println("Queue Front : " + q.front.data);
        System.out.println("Queue Rear : " + q.rear.data);
    }
}

