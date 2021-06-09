'''The count-and-say sequence is a sequence of digit strings defined by the recursive formula:

 -> countAndSay(1) = "1"
 -> countAndSay(n) is the way you would "say" the digit string from countAndSay(n-1), which is then converted into a different digit string.
To determine how you "say" a digit string, split it into the minimal number of groups so that each group is a contiguous section all of the same character. Then for each group, say the number of characters, then say the character. To convert the saying into a digit string, replace the counts with a number and concatenate every saying.

Given a positive integer n, return the nth term of the count-and-say sequence.

Example
Input: n = 4
Output: "1211"
Explanation:
countAndSay(1) = "1"
countAndSay(2) = say "1" = one 1 = "11"
countAndSay(3) = say "11" = two 1's = "21"
countAndSay(4) = say "21" = one 2 + one 1 = "12" + "11" = "1211" '''

class Solution:
    def countAndSay(self, n: int) -> str:
        self.n = n
        if n == 1:
            return "1"
        s = [1,1]
        for i in range(n-2):
            new_s = []
            temp = 1
            for i in range(1,len(s)):
                if(s[i] == s[i-1]):
                    temp+=1
                else:
                    new_s.append(temp)
                    new_s.append(s[i-1])
                    temp = 1
            new_s.append(temp)
            new_s.append(s[-1])
            s = new_s
        ans = ""
        for x in s:
            ans = ans + str(x)
        return ans

