#User function Template for python3

class Solution:
    #Function to count number of ways to reach the nth stair.
    def countWays(self,n):
        
        # def recur(ind):
        #     if (ind==0 or ind==1):
        #         return 1
        #     one_step = recur(ind-1)
        #     two_step = recur(ind-2)
        #     return one_step+two_step
        # return recur(n)
        
        # dp = [-1 for i in range(n+1)]
        # def recur(ind):
        #     if (ind==0 or ind==1):
        #         return 1
        #     one_step = recur(ind-1)
        #     two_step = recur(ind-2)
        #     if dp[ind]!=-1:
        #         dp[ind]
        #     dp[ind] = one_step+two_step
        #     return dp[ind]
        # return recur(n)
        
        # dp = [-1 for i in range(n+1)]
        # dp[0] = 1
        # dp[1] = 1
        # for i in range(2,n+1):
        #     dp[i] = dp[i-1]+dp[i-2]
        
        # return dp[n]%(10**9+7)
        ans = 1        
        prev1 = 1
        prev2 = 1
        for i in range(2,n+1):
            ans = prev1+prev2
            prev2 = prev1
            prev1 = ans
        
        return ans%(10**9+7)


#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys
sys.setrecursionlimit(10**6)

# Contributed by : Nagendra Jha

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        m = int(input())
        ob=Solution()
        print(ob.countWays(m))

# } Driver Code Ends