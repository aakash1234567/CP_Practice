class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """    
        
        ind = -1
        
        for i in range(len(nums)-2,-1,-1):
            if nums[i]<nums[i+1]:
                ind = i
                break

        if ind == -1:
            for i in range(len(nums)//2):
                nums[i], nums[len(nums)-i-1] = nums[len(nums)-i-1], nums[i]
        else:
            for i in range(len(nums)-1,ind,-1):
                if nums[i]>nums[ind]:
                    nums[i], nums[ind] = nums[ind], nums[i]
                    break

            for i in range((len(nums)-ind)//2):
                nums[ind+1+i], nums[len(nums)-i-1] = nums[len(nums)-i-1], nums[ind+1+i]