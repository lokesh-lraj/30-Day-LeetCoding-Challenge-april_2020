def maxSubArray(self, nums: List[int]) -> int:
        
        global_max = local_max = nums[0]
        nums = nums[1:]
        for num in nums:
            local_max = max(num, local_max + num)
            if local_max > global_max :
                global_max = local_max
        return global_max
