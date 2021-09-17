'''
Consider a rat placed at (0, 0) in a square matrix of order N * N. It has to reach the destination at (N - 1, N - 1). Find all possible paths that the rat can take to reach from source to destination. The directions in which the rat can move are 'U'(up), 'D'(down), 'L' (left), 'R' (right). Value 0 at a cell in the matrix represents that it is blocked and rat cannot move to it while value 1 at a cell in the matrix represents that rat can be travel through it.
Note: In a path, no cell can be visited more than one time.

Example 1:

Input:
N = 4
m[][] = {{1, 0, 0, 0},
         {1, 1, 0, 1}, 
         {1, 1, 0, 0},
         {0, 1, 1, 1}}
Output:
DDRDRR DRDDRR
Explanation:
The rat can reach the destination at 
(3, 3) from (0, 0) by two paths - DRDDRR 
and DDRDRR, when printed in sorted order 
we get DDRDRR DRDDRR.

Approach:
The code is well commented.
'''

from typing import List
MAX = 5
# returns if a particular cell is safe to travel
def is_safe(row, col,n,  maze, visited):
    if (row == -1 or row == n or col == -1 or col == n or visited[row][col] or maze[row][col] == 0):
        return False
    return True

# returns the list of all possible paths
def give_path(row: int, col: int, n: int,
                  maze: List[List[int]],
                  visited: List[List[bool]], path: str,
                  path_list: List[str]):
    # check if a cell is safe
    if not is_safe(row, col, n, maze, visited):
        return
    
    # check if we have reached destination
    if row == col == n-1:
        path_list.append(path)
        return
    
    # mark the visited cell
    visited[row][col] = True
    
    # checking in each direction
    if is_safe(row-1, col, n, maze, visited):
        path += 'U'
        give_path(row-1, col, n, maze, visited, path, path_list)
        path = path[:-1]
    if is_safe(row, col+1, n, maze, visited):
        path += 'R'
        give_path(row, col+1, n, maze, visited, path, path_list)
        path = path[:-1]
    if is_safe(row+1, col, n, maze, visited):
        path += 'D'
        give_path(row+1, col, n, maze, visited, path, path_list)
        path = path[:-1]
    if is_safe(row, col-1, n, maze, visited):
        path += 'L'
        give_path(row, col-1, n, maze, visited, path, path_list)
        path = path[:-1]
    
    
        
    # unvisit the cell for further path
    visited[row][col] = False

class Solution:
    def findPath(self, m, n):
        # code here
        # vector to store all the possible paths
        
        visited = [[False for _ in range(5)] for _ in range(n)]
        path = ""
        path_list = []
        give_path(0, 0,n, m, visited, path, path_list)
        
        return sorted(path_list)
        

#{ 
#  Driver Code Starts
#Initial Template for Python 3\

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n = list(map(int, input().strip().split()))
        arr = list(map(int, input().strip().split()))
        
        matrix = [[0 for i in range(n[0])]for j in range(n[0])]
        k=0
        for i in range(n[0]):
            for j in range(n[0]):
                matrix[i][j] = arr[k]
                k+=1
        ob = Solution()
        result = ob.findPath(matrix, n[0])
        if len(result) == 0 :
            print(-1)
        else:
            for x in result:
                print(x,end = " ")
            print()
# } Driver Code Ends
