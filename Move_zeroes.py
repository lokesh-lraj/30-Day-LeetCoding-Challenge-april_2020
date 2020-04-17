def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if 0 in nums:
            
            zi = index_zero = nums.index(0)
            #first_zero = True
            l = len(nums)
            for i in range(zi,l):
                if nums[i] != 0 and i > index_zero:
                    nums[index_zero] = nums[i]
                    nums[i] = 0
                    index_zero = nums.index(0)
