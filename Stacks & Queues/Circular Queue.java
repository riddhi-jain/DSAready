// Problem Statement -> Implementing circular queue
// Logic : On dequeing in normal queues, we end up with garbage space up front which cannot be utlised for further enqueing
// Circular queue solves this problem by enuqueing elements in those garbage spaces 
// Time Complexity : O(1)

package Queues;

public class CircularQueue {
    int capacity;
    int front, rear;
    int arr[] = new int[capacity];
    
    public CircularQueue(int capacity)
    {   
        this.capacity = capacity;
        front = -1;
        rear = -1;
        arr = new int[this.capacity];
    }
    boolean isFull()
    {
        if ((front == 0 && rear == capacity-1)||(rear == (front-1)%(capacity-1)))
        {
            return true;
        }
        else if( front == rear + 1)
    {
        return true;
    }
    return false;
    }

    boolean isEmpty()
    {
        if(front == -1)
        {
            return true;
        }
        return false;

    }
    
    void enqueue(int data)
    {
        if(isFull())
        {       
            System.out.println("Queue is full");
        }
        else if(isEmpty())
        {
            front = 0;
            rear = 0;
            arr[rear] = data;
            System.out.println(data + " HAS BEEN ENQUEUED");
        }
        else {

        
        rear = (rear + 1)%capacity;
        arr[rear] = data;
        System.out.println(data + " HAS BEEN ENQUEUED");
        }
    }
    
    int dequeue()
    {
        if(isEmpty())
        {
            System.out.println(" EMPTY QUEUE ");
            return 0;
        }
        else
        {
            int x = arr[front];
            if(front==rear) 
            {
                front = -1;
                rear = -1;
            } 
            else 
            {
                front =(front+1)%capacity;
            }
        System.out.print(x + " HAS BEEN DEQUEUED ");
        System.out.println(" ");
        return x; 
        }
        
    }

    void peek()
    {
        if(isEmpty())
        {
            System.out.println("Queue is empty");
        }
        System.out.println( "Result of peeking " + arr[front]);
        
    }

    void display()
    {
        int i;
        if(isEmpty())
        {
            System.out.println("QUEUE IS EMPTY");
        }
        else
        {
            System.out.println("________________________");
            System.out.print("Front -> " + front);
            System.out.println(" ");
            System.out.print("Data -> ");
            for(i = front; i!=rear; i = (i+1)%capacity)
            {
                System.out.print(arr[i] + " ");
            }
            System.out.println(arr[i]);
            System.out.println("Rear -> " + rear);
            System.out.println("________________________");
        }
    }
    public static void main(String[] args) {
        CircularQueue queue = new CircularQueue(8);
        queue.enqueue(100);
        queue.enqueue(700);
        queue.enqueue(200);
        queue.enqueue(500);
        queue.enqueue(20);
        queue.enqueue(56);
        queue.enqueue(576);
        queue.enqueue(53);
        queue.enqueue(5046);
        queue.display();
        queue.dequeue();
        queue.display();
        queue.peek();
    }
}
/* 
Output :
100 HAS BEEN ENQUEUED
700 HAS BEEN ENQUEUED
200 HAS BEEN ENQUEUED
500 HAS BEEN ENQUEUED
20 HAS BEEN ENQUEUED
56 HAS BEEN ENQUEUED
576 HAS BEEN ENQUEUED
53 HAS BEEN ENQUEUED
Queue is full
________________________
Front -> 0
Data -> 100 700 200 500 20 56 576 53
Rear -> 7
________________________
100 HAS BEEN DEQUEUED
________________________
Front -> 1
Data -> 700 200 500 20 56 576 53
Rear -> 7
________________________
Result of peeking 700
*/