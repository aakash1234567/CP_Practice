class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        real_sum = len(nums)*(len(nums)+1)//2
        current_sum = sum(nums)
        return real_sum - current_sum