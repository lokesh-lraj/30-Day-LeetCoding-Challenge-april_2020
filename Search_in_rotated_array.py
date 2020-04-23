"""
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).

You are given a target value to search. If found in the array return its index, otherwise return -1.

You may assume no duplicate exists in the array.

Your algorithm's runtime complexity must be in the order of O(log n).

Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4

Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1
"""
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        l = len(nums)
        if not l :
            return -1
        left = 0
        right = l - 1
        first = nums[0]
        
        while left <= right :
            mid = (left + right)//2
            val = nums[mid]
            if val == target :
                return mid
            
            else:
                am_big = val >= first
                target_big = target >= first
                if am_big == target_big:
                    if val < target :
                        left = mid + 1
                    else:
                        right = mid - 1
                        
                else:
                    if am_big :
                        left = mid + 1
                    else:
                        right = mid - 1
        return -1
        
