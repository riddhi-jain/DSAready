'''Given a string S, find the longest palindromic substring in S. Substring of string S: S[ i . . . . j ] where 0 ≤ i ≤ j < len(S). Palindrome string: A string which reads the same backwards. More formally, S is palindrome if reverse(S) = S. Incase of conflict, return the substring which occurs first ( with the least starting index).

Approach:   (using DP)
1. Maintain a boolean table[n][n] that is filled in bottom up manner.
2. The value of table[i][j] is true, if the substring is palindrome, otherwise false.
3. To calculate table[i][j], check the value of table[i+1][j-1], if the value is true and str[i] is same as str[j], then we make table[i][j] true.
Otherwise, the value of table[i][j] is made false.
4. We have to fill table previously for substring of length = 1 and length =2 because 
as we are finding , if table[i+1][j-1] is true or false , so in case of 
(i) length == 1 , lets say i=2 , j=2 and i+1,j-1 doesn’t lies between [i , j] 
(ii) length == 2 ,lets say i=2 , j=3 and i+1,j-1 again doesn’t lies between [i , j]. '''

class Solution:
    def longestPalin(self, S):
        self.S = S
        n = len(S)
        max_len = 1
        table = [[0 for _ in range(n)] for _ in range(n)]
        l0 = []
        # substring of length 1
        for i in range(n):
            table[i][i] = True
            l0.append(S[i])
        
        # substring of length 2
        start = 0
        for i in range(n-1):
            if S[i] == S[i+1]:
                table[i][i+1] = True
                start = i
                max_len = 2
                l0.append(str(S[i] + S[i+1]))
              
        # substring of length more than 2
        for k in range(3, n+1):
            for i in range(0, n-k+1):
                j = i+k-1
                s = ""
                if (S[i] == S[j] and table[i+1][j-1]):
                    table[i][j] = True
                    if k > max_len:
                        max_len = k
                        start = i
                        l0.append(S[start: start+max_len])
                        
        return max(l0, key = len)

if __name__ == '__main__':

    t = int(input())

    for _ in range(t):
        S = input()

        ob = Solution()

        ans = ob.longestPalin(S)

        print(ans)
