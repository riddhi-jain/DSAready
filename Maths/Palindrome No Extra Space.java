// Problem Statement -> Find if the given number is palindrome or not without taking extra space

// Logic : For this solution we take the front and rear of the integer
// If front==rear we slice the front and rear and check for next
// else return NOT PALINDROME

// Time Complexity : O(N)
package Algorithms.Mathematical;

public class PalindromeNoExtraSpace {
    static boolean intIsPalindrome (int data) 
    {   
        // We use this loop to get the appropriate divisor for the front digit
        // Example : 123 needs to be divided by 100 to get dividend as 1 which is the first digit of the number
        int div = 1;
        while(data/div >= 10)
        {   
            div *= 10;
        }

        while(data!=0)
        {
            int front = data/div; // We divide the number by the divisor we got to get the first digit of the number
            int rear = data % 10; // 123%10 gives 3 as remainder which is the last digit
            if( front != rear )
            {
                return false;
            }
                data = (data%div) / 10; 
                // Example : (13231%10000)/10 = 323 
                div /= 100;
                // We are dividing by 100 since 2 digits are dropped by the above line
                // So two tens places also need to removed from the divisor
                // 10000/100 = 100 

        }
        return true;
    }
    public static void main(String[] args) {
        int data = 13231; // Output : True
        System.out.println(
            intIsPalindrome(data));
    }   
}

