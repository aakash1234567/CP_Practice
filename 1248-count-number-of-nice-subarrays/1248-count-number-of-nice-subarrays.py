class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        
        left = 0
        temp = 0
        n = len(nums)
        cnt = 0
        for right in range(n):
            if nums[right]&1:
                temp=0
                k-=1
            while k==0:
                k+=nums[left]&1
                left+=1
                temp+=1
            cnt+=temp
        return cnt