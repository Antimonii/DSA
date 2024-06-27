class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxsub = nums[0]
        currmax = 0 

        for i in nums:
            if currmax < 0:
                currmax = 0
            currmax += i
            maxsub = max(currmax,maxsub)
        
        return maxsub