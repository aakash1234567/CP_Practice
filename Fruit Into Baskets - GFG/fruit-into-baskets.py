#User function Template for python3

class Solution:
    def sumSubarrayMins(self, N, fruits):
        # Code here
        d = {}
        left = 0
        right = 0
        mx = 0
        
        while right<N:
            if fruits[right] not in d:
                d[fruits[right]]=1
            else:
                d[fruits[right]]+=1
            while len(d)>2:
                if d[fruits[left]]==1:
                    d.pop(fruits[left])
                else:
                    d[fruits[left]]-=1
                left+=1
            mx = max(mx,right-left+1)
            right+=1
        return mx
#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input ())
    for _ in range (t):
        N = int(input())
        fruits = list(map(int, input().split()))
        ob = Solution()
        res = ob.sumSubarrayMins(N, fruits)
        print(res)
# } Driver Code Ends