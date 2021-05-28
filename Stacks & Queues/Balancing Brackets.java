// *********Problem Statement***********
// Given a string expr, write a program to examine whether the pairs and
// the orders of  “{“, “}”, “(“, “)”, “[“, “]” are correct in expr
// Logic : We use a stack to push all the open brackets we encounter and when encountering a closed bracket we pop the stack
// until we find the corresponding pair of open bracket
// Time Complexity : O(N)

package Stacks;

import java.util.Stack;

public class BalancingBrackets {
    static boolean areBracketsBalanced( String expr ) {
        
        Stack<Character> stack = new Stack<Character>();
        
        for ( int i = 0; i<expr.length(); i++)
        {
            char x = expr.charAt(i);
            if (x == '(' || x == '{' || x == '[') {
                stack.push(x);
                continue;
            }
            if (stack.isEmpty()){
                return false;
            }
            char check;
            switch(x) {
                case ')':
                check = stack.pop();
                if (check == '{' || check == '[') 
                    return false;
                    break;
                
                case '}':
                check = stack.pop();
                if (check == '(' || check == '[') 
                    return false;
                    break;
                case ']':
                check = stack.pop();
                if (check == '(' || check == '{') 
                    return false;
                    break;
        }
    }
    return(stack.isEmpty());
}
        public static void main (String args[]){
            String expr = "{[()]}";
            
            if (areBracketsBalanced(expr)!=false){
                System.out.println("Balanced");
            }
            else {
            System.out.println("Unbalanced");
            }

        }
 }

    
