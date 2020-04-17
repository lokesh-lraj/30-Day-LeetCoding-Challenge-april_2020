"""
Given a binary array, find the maximum length of a contiguous subarray with equal number of 0 and 1.

Example 1:
Input: [0,1]
Output: 2
Explanation: [0, 1] is the longest contiguous subarray with equal number of 0 and 1.
Example 2:
Input: [0,1,0]
Output: 2
Explanation: [0, 1] (or [1, 0]) is a longest contiguous subarray with equal number of 0 and 1.
"""

class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        
        l = len(nums)
        ans = 0
        frst = {}
        frst[0] = 0
        pref = 0
        
        for i in range(l):
            pref += (1 if nums[i] == 1 else -1)
            if pref in frst :
                ans = max(ans, i + 1 - frst[pref])
            else :
                frst[pref] = i + 1
        return ans
        
                    
