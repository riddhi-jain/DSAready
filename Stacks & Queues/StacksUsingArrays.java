package Stacks;
import java.util.Scanner;

public class StacksUsingArrays {
    int top; // pointer to track the topmost pointer
    static final int MAX = 1000; // to prevent stack overflow for our top pointer
    int arr[] = new int[MAX];
    boolean isEmpty() {
        return (top < 0);
    }
    StacksUsingArrays() {
        top = -1;
    }
    boolean push(int x) {
        if(top >= MAX-1) {
            System.out.println("Stack Overflow");
            return false;
        }
        else {
            arr[++top] = x;
            System.out.println(x + " Is pushed into the stack ");
            return true;
        }
    }
    int pop() {
        if (top<0) {
            System.out.println("Stack underflow");
            return 0;
        }
        else {
            int x = arr[top--];
            return x;
        }

    }
    int peek() {
        if (top<0) {
            System.out.println("Stack Underflow");
            return 0;
        }
        else {
            int x = arr[top];
            return x;
        }
    }
public static void main(String[] args) {
    StacksUsingArrays s = new StacksUsingArrays();
    Scanner sc = new Scanner(System.in);
    System.out.println("Number of elements you want in the stack");
    int NumberOfOperations = sc.nextInt();
    for ( int i = 0; i< NumberOfOperations; i++) {
        System.out.println("Enter the number you wanna push");
        int number = sc.nextInt();
        s.push(number);
    }
    System.out.println(s.pop() + "Popped from the stack");
    
}

}
