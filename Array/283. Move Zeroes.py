class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        p = 0 
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[i],nums[p] = nums[p],nums[i]
                p += 1
        