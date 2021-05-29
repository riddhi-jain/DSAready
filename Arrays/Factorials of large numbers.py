'''Given an integer N, find its factorial. N can be a very large number. 

Approach:
using dynamic programming, we store the factorial in a dp array'''



class Solution:
    def factorial(self, n):
        self.n = N
        dp = [1]*(n+1)
        for i in range(1, n+1):
            dp[i] = dp[i-1]*i
        return list(map(int, str(dp[n])))

if __name__ == '__main__':
    t=int(input())
    for _ in range(t):
        N = int(input())
        ob = Solution()
        ans = ob.factorial(N);
        for i in ans:
            print(i,end="")
        print()
    
