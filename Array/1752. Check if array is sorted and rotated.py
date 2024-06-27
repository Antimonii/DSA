class Solution:
    def check(self, nums: List[int]) -> bool:
        n = len(nums)
        r = sorted(nums)

        for i in range(n):
            if nums[i:] + nums[:i] == r:
                return True
        return False