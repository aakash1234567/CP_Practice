#User function Template for python3
class Solution:
	
	def findMaxSum(self,arr, n):
		# code here
# 		def recur(ind):
# 		    if ind<0:
# 		        return 0
# 		    if ind==0:
# 		        return arr[ind]
		    
# 		    pick = recur(ind-2) + arr[ind]
# 		    notPick = recur(ind-1)
# 		    return max(pick, notPick)
        
#         return recur(n-1)
        
    #     dp = [-1 for i in range(n)]
    #     def recur(ind):
		  #  if ind<0:
		  #      return 0
		  #  if ind==0:
		  #      return arr[ind]
		  #  if dp[ind] != -1:
		  #      return dp[ind]
		  #  pick = recur(ind-2) + arr[ind]
		  #  notPick = recur(ind-1)
		  #  dp[ind] = max(pick, notPick)
		  #  return dp[ind]
        
    #     return recur(n-1)
    
        
        # dp = [-1 for i in range(n)]
        # dp[0] = arr[0]
        
        # for ind in range(1,n):
        #     pick = arr[ind]
        #     if ind-2>=0: pick+=dp[ind-2]
        #     notpick = dp[ind-1]
        #     dp[ind] =  max(pick, notpick)
    
        # return dp[n-1]
        
        prev1 = arr[0]
        prev2 = 0

        for ind in range(1,n):
            pick = arr[ind]
            if ind-2>=0: pick+=prev2
            notpick = prev1
            prev2 = prev1
            prev1 =  max(pick, notpick)
    
        return prev1

#{ 
 # Driver Code Starts
#Initial Template for Python 3




if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.findMaxSum(arr, n)
        print(ans)
        tc -= 1

# } Driver Code Ends