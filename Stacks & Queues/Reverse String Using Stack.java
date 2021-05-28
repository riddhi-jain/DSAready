// *********Problem Statement***********
// Reversing a String using a Stack.
// logic :popping a string after pushing it to a stack gives the string in a reverse
// order because of LIFO concept
// Time Complexity : O(N)

package Stacks;

import java.util.Stack;

public class ReverseStringUsingStack {
    static String ReverseString( String expr) {
        String result = new String("");

        Stack<Character>stack = new Stack<>();
        for (int i = 0; i<expr.length() ; i++) {
            char c = expr.charAt(i);
            stack.push(c);
        }
        while(!stack.isEmpty()) {
            result += stack.pop();    
        }
        return result;
    }
    public static void main(String[] args) {
        String expr = "abcdefghijklmnopqrstuvwxyz";
        System.out.println(ReverseString(expr));
    }
    
}
