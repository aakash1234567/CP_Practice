#User function Template for python3

class Solution:
    def minimumEnergy(self, height, n):
        # Code here
        
        # def recur(ind):
        #     if (ind==0):
        #         return 0
                
        #     one_step = recur(ind-1) + abs(height[ind]-height[ind-1])
        #     two_step = 10000
        #     if ind-2>=0:
        #         two_step = recur(ind-2) + abs(height[ind]-height[ind-2])

        #     return min(one_step, two_step)
        
        # return recur(n-1)
        
        # dp = [-1 for i in range(n)]
        # def recur(ind):
        #     if (ind==0):
        #         return 0
        #     if dp[-1]!=-1:
        #         return dp[ind]
        #     one_step = recur(ind-1) + abs(height[ind]-height[ind-1])
        #     two_step = 10000
        #     if ind-2>=0:
        #         two_step = recur(ind-2) + abs(height[ind]-height[ind-2])
        #     dp[ind] = min(one_step, two_step)
        #     return dp[ind]
        
        # return recur(n-1)
        
        # dp = [-1 for i in range(n)]
        
        # dp[0] = 0
        
        # for ind in range(1,n):
        #     one_step = dp[ind-1] + abs(height[ind]-height[ind-1])
        #     two_step = 10000
        #     if ind-2>=0:
        #         two_step = dp[ind-2] + abs(height[ind]-height[ind-2])
        #     dp[ind] = min(one_step, two_step)
            
        # return dp[n-1]
        
        prev1 = 0
        prev2 = 0
        
        for ind in range(1,n):
            one_step = prev1 + abs(height[ind]-height[ind-1])
            two_step = 10000
            if ind-2>=0:
                two_step = prev2 + abs(height[ind]-height[ind-2])
            prev2 = prev1
            prev1 = min(one_step, two_step)
            
        return prev1
        
        
#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        height = list(map(int, input().split()))
        ob = Solution()
        print(ob.minimumEnergy(height, n))
# } Driver Code Ends