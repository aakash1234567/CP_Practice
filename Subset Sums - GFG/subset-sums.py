#User function Template for python3
class Solution:
	def subsetSums(self, arr, N):
		# code here
        def recur(ind, sm):
            if ind==N:
                ans.append(sm)
                return
            recur(ind+1,sm+arr[ind])
            
            recur(ind+1, sm)
        
        ans = []
        recur(0, 0)
        return ans

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    T=int(input())
    for i in range(T):
        N = int(input())
        arr = [int(x) for x in input().split()]
        ob = Solution()
        ans = ob.subsetSums(arr, N)
        ans.sort()
        for x in ans:
            print(x,end=" ")
        print("")

# } Driver Code Ends