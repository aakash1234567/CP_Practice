#User function Template for python3
class Solution:

	def print2largest(self,arr, n):
		# code here
		mx = arr[0]
		smx = -1
		
		for i in range(1,n):
		    if arr[i]>mx:
		        smx=mx
		        mx=arr[i]
		    if arr[i]>smx and arr[i]!=mx:
		        smx=arr[i]
		        
		return smx

#{ 
 # Driver Code Starts
#Initial Template for Python 3



if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.print2largest(arr, n)
        print(ans)
        tc -= 1

# } Driver Code Ends