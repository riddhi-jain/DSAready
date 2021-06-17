'''Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]

Approach:
We can start an opening bracket if we still have one (of n) left to place. And we can start a closing bracket if it would not exceed the number of opening brackets.
We maintain a stack to add brackets as per above two conditions untill stack.size != 2*n and backtrack to previous state to continue adding brackets again.'''

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        def backtrack(S = [], left = 0, right = 0):
            # base case
            if len(S) == 2 * n:
                ans.append("".join(S))
                return
            # condition 1
            if left < n:
                S.append("(")
                backtrack(S, left+1, right)
                S.pop()
            # condition 2
            if right < left:
                S.append(")")
                backtrack(S, left, right+1)
                S.pop()
        backtrack()
        return ans


