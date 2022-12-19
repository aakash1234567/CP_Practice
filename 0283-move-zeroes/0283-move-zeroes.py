class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        z = 0
        for i in range(len(nums)):
            if nums[z]==0 and nums[i]!=0:
                nums[z],nums[i]=nums[i],nums[z]
                z+=1
            elif nums[z]!=0:
                z+=1
        