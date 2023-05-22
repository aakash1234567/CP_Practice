class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        mp = {}
        maxElements = 1
        
        for i in nums:
            if i in mp:
                mp[i]+=1
                maxElements = max(maxElements, mp[i])
            else:
                mp[i]=1
                
        bucket = [[] for i in range(maxElements)] 
        
        for val in mp:
            bucket[mp[val]-1].append(val)
        
        res = []
        for i in range(maxElements-1, -1, -1):
            j = len(bucket[i])-1
            while len(bucket[i]):
                if len(res)==k:
                    break
                res.append(bucket[i][j])
                bucket[i].pop()
                j-=1
                
            if len(res)==k:
                break
        return res