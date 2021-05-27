package Stacks;

import static java.lang.Character.isDigit;

import java.util.Stack;

public class PostfixEval {
    static int postFixEvaluation(String expr) {
        Stack<Integer> stack = new Stack<>();

        for (int i = 0; i< expr.length(); i++) {
            char c = expr.charAt(i);
            if(Character.isDigit(c)) {
                stack.push(c - '0');
            }
            else {
                int val1 = stack.pop();
                int val2 = stack.pop();
            
            switch(c)
            {
                case '*':
                stack.push(val2 * val1);
                break;
                case '+':
                stack.push(val2 + val1);
                break;
                case '-':
                stack.push(val2 - val1);
                break;
                case '/':
                stack.push(val1 / val2);
                break;
            }   
        }
            

        }
        return stack.pop();

    }
    public static void main(String[] args) {
        String expr = "231*+9-";
        System.out.println(postFixEvaluation(expr));
    }
}