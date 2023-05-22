#User function Template for python3
class Solution:

	def immediateSmaller(self,arr,n):
		# code here
		
		nxt = arr[-1]
		arr[-1] = -1
		for i in range(n-2,-1,-1):
		    curr = arr[i]
		    if curr>nxt:
		        arr[i]=nxt
		    else:
		        arr[i]=-1
		    nxt = curr


#{ 
 # Driver Code Starts
if __name__ == '__main__':
    tcs=int(input())

    for _ in range(tcs):
        n=int(input())
        arr=[int(x) for x in input().split()]
        ob = Solution()
        ob.immediateSmaller(arr,n)
        for x in arr:
            print(x, end=" ")
        print()
# } Driver Code Ends