"""
Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by 

connecting adjacent lands horizontally or vertically.You may assume all four edges of the grid are all surrounded by water.

Input:
11110
11010
11000
00000

Output: 1

Input:
11000
11000
00100
00011

Output: 3
"""

class Solution:
    def inside(self, r, c, H, W):
        return 0 <= r < H and 0 <= c < W
    
    def numIslands(self, grid: List[List[str]]) -> int:
    
        if not grid or not grid[0]:
            return 0
        
        H = len(grid)
        W = len(grid[0])
        
        moves = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        visited = [[False for _ in range(W)]for _ in range(H)]
        queue = []
        
        ans = 0
        
        for row in range(H):
            for column in range(W):
                if not visited[row][column] and grid[row][column] == '1':
                    ans += 1
                    queue.append([row, column])
                    visited[row][column] = True
                    
                    while queue:
                        p = queue[0]
                        queue.pop(0)
                        for move in moves:
                            x = p[0] + move[0]
                            y = p[1] + move[1]
                            
                            if self.inside(x, y, H, W) and not visited[x][y] and grid[x][y] == '1':
                                queue.append([x, y])
                                visited[x][y] = True
        return ans
