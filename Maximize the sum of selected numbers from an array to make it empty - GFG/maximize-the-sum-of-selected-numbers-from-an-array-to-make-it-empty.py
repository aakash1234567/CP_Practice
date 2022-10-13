#User function Template for python3

class Solution:
    
    def maximizeSum (self,arr, n) : 
        #Complete the function
        dp = {}
        for i in range(n):
            if arr[i] in dp:
                dp[arr[i]]+=1
            else:
                dp[arr[i]]=1
        
        sm = 0
        for i in range(n-1,-1,-1):
            if dp[arr[i]]:
                dp[arr[i]]-=1
                sm+=arr[i]
                if arr[i]-1 in dp and dp[arr[i]-1]:
                    dp[arr[i]-1]-=1
        return sm


#{ 
 # Driver Code Starts
#Initial Template for Python 3


for _ in range(0,int(input())):
    n = int(input())
    arr = list(map(int, input().strip().split()))
    arr.sort()
    ob=Solution()
    
    ans = ob.maximizeSum(arr, n)
    print(ans)

    





# } Driver Code Ends