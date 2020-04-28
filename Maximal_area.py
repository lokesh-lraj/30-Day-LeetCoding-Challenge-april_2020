"""
Given a 2D binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.

Example:

Input: 

1 0 1 0 0
1 0 1 1 1
1 1 1 1 1
1 0 0 1 0

Output: 4
"""
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if not matrix or not matrix[0]:
            return 0
        H = len(matrix)
        W = len(matrix[0])
        dp = [[0 for _ in range(W)]for _ in range(H)]
        ans = 0
        for row in range(H):
            for column in range(W):
                if matrix[row][column] == '1':
                    dp[row][column] = 1
                    if row > 0 and column > 0:
                        dp[row][column] += min(dp[row-1][column], dp[row][column-1], dp[row-1][column-1])
                    ans = max(ans, dp[row][column])
        return ans ** 2
