'''
Given an m x n binary matrix mat, return the distance of the nearest 0 for each cell.
The distance between two adjacent cells is 1.

Example:
0 0 0
0 1 0 
0 0 0

Input: mat = [[0,0,0],[0,1,0],[0,0,0]]
Output: [[0,0,0],[0,1,0],[0,0,0]]

Explaination:
* Iterate over the matrix from top to bottom-left to right:
 - Update dist[i][j] = min( dist[i][j], min( dist[i][j-1], dist[i-1][j]) + 1) i.e., minimum of the current dist and distance from top or left neighbor +1, that would have been already calculated previously in the current iteration.
* Now, we need to do the back iteration in the similar manner: from bottom to top-right to left:
 - Update dist[i][j] = min( dist[i][j], min( dist[i][j+1], dist[i+1][j]) + 1) i.e. minimum of current dist and distances calculated from bottom and right neighbors, that would be already available in current iteration.
'''


class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        rows = len(mat)
        if rows == 0:
            return mat
        cols = len(mat[0])
        dp = [[float("inf")]*cols for _ in range(rows)]
        
        for i in range(rows):
            for j in range(cols):
                if mat[i][j] == 0:
                    dp[i][j] = 0
                else:
                    if i > 0:
                        dp[i][j] = min(dp[i][j], dp[i-1][j] + 1)
                    if j > 0:
                        dp[i][j] = min(dp[i][j], dp[i][j-1] + 1)
        for i in range(rows-1,-1, -1):
            for j in range(cols-1, -1, -1):
                if i < rows -1:
                    dp[i][j] = min(dp[i][j], dp[i+1][j] + 1)
                if j < cols - 1:
                    dp[i][j] = min(dp[i][j], dp[i][j+1] + 1)
        return dp
        
