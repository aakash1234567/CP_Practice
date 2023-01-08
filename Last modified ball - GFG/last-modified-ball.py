#User function Template for python3

class Solution():
    def solve(self, N, A):
        #your code here
         
        ans = N
        for i in range(N-1,-1,-1):
            if 1+A[i]<=9:
                ans = i+1
                break
        return ans

#{ 
 # Driver Code Starts
#Initial Template for Python 3

for _ in range(int(input())):
    n = int(input())
    array=[int(i) for i in input().split()]
    obj = Solution()
    print(obj.solve(n, array))
# } Driver Code Ends