#User function Template for python3
class Solution:

	def count(self,arr, n, x):
		# code here
		left = 0
		right = n-1
		f = -1
		
		while left<=right:
		    mid = (right+left)//2
		    if arr[mid]==x:
		        f=mid
		        right=mid-1
            elif arr[mid]>x:
                right=mid-1
            else:
                left=mid+1
        
        if f<0:
            return 0
        
        left = 0
		right = n-1
		l = -1
		
		while left<=right:
		    mid = (right+left)//2
		    if arr[mid]==x:
		        l=mid
		        left=mid+1
            elif arr[mid]>x:
                right=mid-1
            else:
                left=mid+1
        return l-f+1

#{ 
 # Driver Code Starts
#Initial Template for Python 3




if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n, x = list(map(int, input().strip().split()))
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.count(arr, n, x)
        print(ans)
        tc -= 1

# } Driver Code Ends