class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        cnt = 0
        temp = 0
        for i in range(len(nums)):
            if nums[i]==1:
                temp+=1
            else:
                cnt = max(cnt,temp)
                temp=0
        return max(cnt,temp)
                