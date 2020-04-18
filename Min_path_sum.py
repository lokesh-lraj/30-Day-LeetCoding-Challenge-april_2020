"""

Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.

Example:

Input:
[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
Output: 7
Explanation: Because the path 1→3→1→1→1 minimizes the sum.

"""

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        columns = len(grid[0])
        path = [[None for _ in range(columns)]for _ in range(rows)]
        path[0][0] = grid[0][0]
        #print(path)
        for i in range(1, rows):
            path[i][0] = path[i-1][0] + grid[i][0]
            
        for j in range(1, columns):
            path[0][j] = path[0][j-1] + grid[0][j]
            
            
        for i in range(1, rows):
            for j in range(1, columns):
                path[i][j] = min(path[i][j-1], path[i-1][j]) + grid[i][j]
                
        return path[-1][-1]
