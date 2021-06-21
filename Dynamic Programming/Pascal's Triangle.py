'''Given an integer numRows, return the first numRows of Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown at : https://upload.wikimedia.org/wikipedia/commons/0/0d/PascalTriangleAnimated2.gif

Example :

Input: numRows = 5
Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]'''

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        self.numRows = numRows
        if numRows == 1:return [[1]]
        elif numRows == 2:return [[1],[1,1]]
        else:
            dp = [0]*(numRows)
            dp[0] = [1]
            dp[1] = [1,1]
            for x in range(2, numRows):
                arr = dp[x-1]
                l1 = []
                for i in range(1, len(arr)):
                    l1.append(arr[i] + arr[i-1])
                dp[x] = [1] + l1 + [1]
            return dp
