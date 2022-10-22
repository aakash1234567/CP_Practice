class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        leftsum = 0
        total = sum(nums)
        n = len(nums)
        
        for i in range(n):
            if leftsum==total-leftsum-nums[i]:
                return i
            else:
                leftsum+=nums[i]
            
        return -1