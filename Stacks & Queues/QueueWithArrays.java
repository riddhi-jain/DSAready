// Problem Statemenet : Implement Queue data structure with an array (Linear solution)
// Time Complexity : O(1)
// Logic : For enqueing we incremement the rear pointer and incremement the size 
//         For dequeing we increment the front pointer and decrement the size
package Queues;

public class QueueWithArrays {
    int capacity; // This is the maximum size the queue can get
    int size, front, rear; // We define the dynamic size and front and rear pointers for the queue
    int[] array; 

    public QueueWithArrays(int capacity) {
        this.capacity = capacity;
        array = new int[capacity];  
        front = this.size = 0;
        rear = capacity - 1; 
    }
    
    boolean isFull(QueueWithArrays queue) 
    {
        return(queue.size == queue.capacity);
    }

    boolean isEmpty(QueueWithArrays queue) 
    {
        return(queue.size == 0);
    }
    
    void enqueue(int data) {
        if(isFull(this)) {
            return;
        }
        this.rear = (this.rear + 1)% this.capacity; // Inorder to get the index with respect to capactity we mod this.capacity
        this.array[this.rear] = data;
        this.size = size + 1; // Since the size of the array increases on adding an element
        System.out.println(data + " is enqueued intot the Queue");
    }
    int dequeue() {
        if(isEmpty(this)) {
            return Integer.MIN_VALUE;
        }
        int data = array[front];
        this.front = (this.front + 1)%this.capacity;
        this.size = this.size - 1; // Since dequeing the element reduces the size for the array by 1
        return data;

    }
    int front() {
        return(this.array[front]);
    }
    int rear() {
        return(this.array[rear]);
    }
    public static void main(String[] args) {
        QueueWithArrays queue = new QueueWithArrays(1000);
 
        queue.enqueue(10);
        queue.enqueue(20);
        queue.enqueue(30);
        queue.enqueue(40);
 
        System.out.println(queue.dequeue()
                           + " dequeued from queue\n");
 
        System.out.println("Front item is "
                           + queue.front());
 
        System.out.println("Rear item is "
                           + queue.rear());
    }
}
// Output : 
/* 
10 is enqueued intot the Queue
20 is enqueued intot the Queue
30 is enqueued intot the Queue
40 is enqueued intot the Queue
10 dequeued from queue

Front item is 20
Rear item is 40
*/