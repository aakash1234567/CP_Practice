class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
        def recur(ind):
            ans.append(temp[:])
            for i in range(ind,len(nums)):
                if (i!=ind and nums[i]==nums[i-1]):
                    continue
                temp.append(nums[i])
                recur(i+1)
                temp.pop()
            
        ans = []
        nums.sort()
        temp = []
        recur(0)
        return ans