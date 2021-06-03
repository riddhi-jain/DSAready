'''Given a string S. The task is to print all permutations of a given string.
Example:

Input: ABC
Output:
ABC ACB BAC BCA CAB CBA

Approach:
Write a recursive function that employs swap to swap every character with every other character so as to generate all permutations.'''


l0 = []
def permute(s, ans):
    if (len(s) == 0):
        l0.append(ans)
    for i in range(len(s)):
        char = s[i]
        remain = s[:i] + s[i+1:]
        permute(remain, ans + char)
class Solution:
    def find_permutation(self, S):
        # Code here
        self.S = S
        answer = ""
        permute(S, answer)
        return (sorted(l0))


if __name__ == '__main__':
	t=int(input())
	for i in range(t):
		S=input()
		ob = Solution()
		ans = ob.find_permutation(S)
		for i in ans:
			print(i,end=" ")
		print()
