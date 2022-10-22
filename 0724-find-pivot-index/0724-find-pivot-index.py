class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
#       pivot should not be considered in sum
        leftsum = 0
        total = sum(nums)
        
        for i,v in enumerate(nums):
            if leftsum==total-leftsum-v:
                return i
            else:
                leftsum+=v
            
        return -1