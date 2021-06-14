'''Given two strings s and t, return true if s is a subsequence of t, or false otherwise.
A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).

Example :
Input: s = "abc", t = "ahbgdc"
Output: true

Approach 1(Two pointers):
1.use two pointers i and j to iterate through s and t respectively.
2.if at any iteration, s[i] == t[j], increment both i and j
3.else increment only j
4.if i == s.size(), return true 

Approach 2(DP):
1. checking both given strings for their longest common subsequence
2. If the length of longest common subsequence is equal to the smaller string(s), return true.

Following is the solution class for approach 2.'''

def lcs(s1, s2):
    m, n = len(s1), len(s2)
    dp = [[0 for _ in range(n+1)] for _ in range(m+1)]
    for i in range(1,m+1):
        for j in range(1, n+1):
            if s1[i-1] == s2[j-1]:dp[i][j] = dp[i-1][j-1] + 1
            else:dp[i][j] = max(dp[i][j-1], dp[i-1][j])
    return dp[m][n]
    
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        self.s = s
        self.t = t
        if lcs(s,t) == len(s):return True
        else:return False
