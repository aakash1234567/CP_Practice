class Solution:
    def tribonacci(self, n: int) -> int:
        def solve(n):
            if dp[n]!=-1:
                return dp[n]
            dp[n-1] = solve(n-1)
            dp[n-2] = solve(n-2)
            dp[n-3] = solve(n-3)
            return dp[n-1]+dp[n-2]+dp[n-3]
        if n==0:
            return 0
        if n==1:
            return 1
        if n==2:
            return 1
        dp = [-1]*(n+1)
        dp[0]=0
        dp[1]=1
        dp[2]=1
        
        return solve(n)