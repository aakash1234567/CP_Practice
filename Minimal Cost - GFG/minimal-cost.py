#User function Template for python3

class Solution:
    def minimizeCost(self, height, n, k):
        # def recur(ind):
        #     if ind==0:
        #         return 0
            
        #     val = 1000000
        #     for i in range(1,k+1):
        #         if ind-i<0:
        #             break
        #         step = recur(ind-i) + abs(height[ind]-height[ind-i])
        #         val = min(val, step)
        #     return val
        
        # return recur(n-1)


        # dp = [-1 for i in range(n)]
        # def recur(ind):
        #     if ind==0:
        #         return 0
        #     if dp[ind]!=-1:
        #         dp[ind]
        #     val = 1000000
        #     for i in range(1,k+1):
        #         if ind-i<0:
        #             break
        #         step = recur(ind-i) + abs(height[ind]-height[ind-i])
        #         val = min(val, step)
        #         dp[ind] = val
        #     return dp[ind]
        
        # return recur(n-1)
        
        dp = [-1 for i in range(n)]
        dp[0] = 0
        
        for i in range(1, n):
            val = 1000000
            for j in range(1,k+1):
                if i-j<0:
                    break
                step = dp[i-j] + abs(height[i]-height[i-j])
                val = min(val, step)
                dp[i] = val
        return dp[n-1]

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n, k = map(int, input().split())
        height = list(map(int, input().split()))
        ob = Solution()
        print(ob.minimizeCost(height, n, k))
# } Driver Code Ends