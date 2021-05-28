'''Given a string, find the length of the longest repeating subsequence such that the two subsequences don't have same string character at the same position, i.e., any i'th character in the two subsequences shouldn't have the same index in the original string.

Approach:
usingg dp approach for LCS(Longest Common Subsequence)'''
 

class Solution:
	def LongestRepeatingSubsequence(self, s):
		# Code here
		self.s = s
		n = len(s)
		dp = [[0 for _ in range(n+1)] for _ in range(n+1)]
		for i in range(1, n+1):
		    for j in range(1, n+1):
		        if (s[i-1] == s[j-1] and i!= j):dp[i][j] = dp[i-1][j-1] + 1
		        else:dp[i][j] = max(dp[i-1][j], dp[i][j-1])
		return dp[n][n]

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		str = input()
		ob = Solution()
		ans = ob.LongestRepeatingSubsequence(str)
		print(ans)

