#User function Template for python3
class Solution:

	def rowWithMax1s(self,arr, n, m):
		# code here
		
		def search(index,start,end):
		    ans=-1
		    while start<=end:
		        mid = (end+start)//2
                if arr[index][mid]==1:
                    ans=mid
                    end=mid-1
                else:
                    start=mid+1
            return ans
        mx = -1
        ind = -1
        for i in range(n):
            t = search(i,0,m-1)
            if t!=-1:
                if mx < m-t:
                    mx = m-t
                    ind = i
            if mx == m:
                break
        return ind

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n, m = list(map(int, input().strip().split()))
        
        inputLine = list(map(int, input().strip().split()))
        arr = [[0 for j in range(m)] for i in range(n)]
        
        for i in range(n):
            for j in range(m):
                arr[i][j] = inputLine[i * m + j]
        ob = Solution()
        ans = ob.rowWithMax1s(arr, n, m)
        print(ans)
        tc -= 1

# } Driver Code Ends