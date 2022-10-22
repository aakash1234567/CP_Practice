class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        cnt = {}
        
        for v in nums:
            if v in cnt:
                return True
            else:
                cnt[v]=1
        return False