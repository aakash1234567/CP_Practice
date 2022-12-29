#User function Template for python3

class Solution:
    def nextPermutation(self, N, arr):
        # code here
        # 4 steps => 
        # 1.) reverse loop and check for a[i] < a[i+1] => ind1 
        # 2.) reverse loop and check for a[i] > a[ind1] => ind2
        # 3.) swap ind1 and ind2 
        # 4.) reverse ind1+1 to last
        def reverse(i,j):
            while i<j:
                arr[i],arr[j]=arr[j],arr[i]
                i+=1
                j-=1
            
        if len(arr)<=1:
            return arr
        i = len(arr) - 2
        while i>=0 and arr[i] >= arr[i+1]:
            i-=1
        if i>=0:
            j = len(arr)-1
            while arr[j] <= arr[i]:
                j-=1
            arr[i],arr[j]=arr[j],arr[i]
        
        reverse(i+1,N-1)
        return arr


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        arr = input().split()
        for i in range(N):
            arr[i] = int(arr[i])
        
        ob = Solution()
        ans = ob.nextPermutation(N, arr)
        for i in range(N):
            print(ans[i],end=" ")
        print()
# } Driver Code Ends