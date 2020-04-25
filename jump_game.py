"""
Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Determine if you are able to reach the last index.

Example 1:

Input: [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
Example 2:

Input: [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what. Its maximum
             jump length is 0, which makes it impossible to reach the last index.
"""

class Solution:
    def canJump(self, jumps: List[int]) -> bool:
        jump_len = len(jumps)
        # Actual jump_len is one less than jump_len 
        dp = ["Bad"] * (jump_len - 1) + ['Good']
        prev_indx = jump_len - 1
        
        for i in range(prev_indx - 1, -1, -1):
            if jumps[i] >= prev_indx - i:
                dp[i] = 'Good'
                prev_indx = i
        if dp[0] == 'Good':
            return True
        return False
