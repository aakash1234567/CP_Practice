class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ans = 0
        mx=float('-inf')
        for i in range(len(nums)):
            ans+=nums[i]
            if ans>mx:
                mx=ans
            if ans<0:
                ans=0
        return mx
        