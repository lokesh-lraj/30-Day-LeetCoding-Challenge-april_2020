"""

Given an array nums of n integers where n > 1,  return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].

Example:

Input:  [1,2,3,4]
Output: [24,12,8,6]

"""

import math
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        count = nums.count(0)
        length = len(nums)
        
        if count :
            if count > 1 :
                nums = [0] * length
                return nums
            
            product = 1
            for elem in nums:
                if elem != 0:
                    product *= elem
                
            for i in range(length):
                if nums[i] != 0:
                    nums[i] = 0
                else :
                    nums[i] = product
            return nums
                         
        product = math.prod(nums)
        for i in range(length):
            nums[i] = product // nums[i]
        return nums
        
