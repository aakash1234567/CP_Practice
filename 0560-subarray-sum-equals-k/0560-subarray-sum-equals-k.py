class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        dp = {}
        sm = 0
        cnt = 0
        # map to store sum: times https://youtu.be/9fjGM0d1YQQ
        dp[sm] = 1
        
        for i in range(len(nums)):
            sm+=nums[i]
            
            if sm-k in dp:
                cnt += dp[sm-k]
            if sm in dp:
                dp[sm]+=1
            else:
                dp[sm]=1
                
        return cnt
        