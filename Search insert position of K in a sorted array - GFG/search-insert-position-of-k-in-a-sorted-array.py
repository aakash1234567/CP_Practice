#User function Template for python3

class Solution:
    def searchInsertK(self, arr, N, k):
        # code here
        left = 0
        right = N-1
        ans = 0
        while left<=right:
            mid = (left+right)//2
            if arr[mid]==k:
                return mid
            elif arr[mid]>k:
                right=mid-1
            else:
                left=mid+1
                ans=left

        return ans


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range (t):
        N = int(input())
        Arr = input().split()
        for itr in range(N):
            Arr[itr] = int(Arr[itr])
        k = int(input())
        ob = Solution()
        print(ob.searchInsertK(Arr, N, k))
# } Driver Code Ends