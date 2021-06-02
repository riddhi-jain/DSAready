'''Given a non-empty 2D array grid of 0's and 1's, an island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.
Find the maximum area of an island in the given 2D array. (If there is no island, the maximum area is 0.)

Approach:
->To explore the island, we find out all lands connected to a land, by recursively searching positions in the top, bottom, left and right. Each land occupies an area with value 1.
->Once we land on an island (our current position is a land), to mark it as visited, we simply remove the visited island from the grid by sinking the land (mark land as water), and recursively sinking all connected lands around it.
->If we find an island,
We explore the island.
Sum the area of all lands in the island to find the total area.
Sink the island, so we don’t visit it again.
We update the maximum area, if the island’s area is bigger than the biggest island that we had found so far.'''

def getAreaOfIsland(i: int, j: int, grid: List[List[int]]):
    if((i<0) or (i>=len(grid)) or (j<0) or (j>=len(grid[i])) ):
        return 0
if(grid[i][j] == 1):
        grid[i][j]=0
        return 1 + (
            getAreaOfIsland(i+1, j, grid)
            + getAreaOfIsland(i-1, j, grid)
            + getAreaOfIsland(i, j-1, grid) 
            + getAreaOfIsland(i, j+1, grid) 
        )
    return 0
def maxAreaOfIsland(grid: List[List[int]]) -> int:
    max_val = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            max_val = max(max_val, getAreaOfIsland(i, j, grid))
    return max_val
