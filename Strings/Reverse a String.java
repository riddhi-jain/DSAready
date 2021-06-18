// Question-:Write a function that reverses a string. The input string is given as an array of characters s.

 

// Example 1:

// Input: s = ["h","e","l","l","o"]
// Output: ["o","l","l","e","h"]

// Example 2:

// Input: s = ["H","a","n","n","a","h"]
// Output: ["h","a","n","n","a","H"]

// Approach-: Take a temp variable and keep swapping the first and the last element 
// till both the pointers cross.



// Solution



class Solution {
    public void reverseString(char[] s) {
        int n=s.length-1;
        int i=0;
        while(i<n){
            char temp=s[i];
            s[i]=s[n];
            s[n]=temp;
            i++;
            n--;
        }
        
    }
}
