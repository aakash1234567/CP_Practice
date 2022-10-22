class Solution:
    def fib(self, n: int) -> int:
        def solve(n):
            if dp[n]!=-1:
                return dp[n]
            dp[n-1] = solve(n-1)
            dp[n-2] = solve(n-2)
            return dp[n-1]+dp[n-2]
            
        if n==0:
            return 0
        if n==1:
            return 1
        dp = [-1]*(n+1)
        dp[0] = 0
        dp[1] = 1
        return solve(n)