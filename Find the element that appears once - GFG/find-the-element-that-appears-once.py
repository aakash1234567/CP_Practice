#User function Template for python3
class Solution:
    def search(self, A, N):
        # your code here
        
        start = 0
        end = N-1
        
        while start<end:
            mid = (end+start)//2
            if mid%2==1:
                mid-=1
            if A[mid] == A[mid+1]:
                start=mid+2
            else:
                end = mid
        return A[start]

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
	t = int (input ())
	for tc in range (t):
		n = int (input ())
		arr = list(map(int, input().split()))
		ob = Solution()
		print(ob.search(arr, n)) 
# } Driver Code Ends