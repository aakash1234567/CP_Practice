#User function Template for python3

class Solution:
    def leftRotate(self, arr, n, d):
        # code here
        
        def reverse(start, end):
            while start<end:
                arr[start], arr[end] = arr[end], arr[start]
                start+=1
                end-=1
        d%=n
        reverse(0,d-1)
        reverse(d, n-1)
        reverse(0,n-1)


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        d = int(input())
        ob = Solution()
        ob.leftRotate(arr, n, d)
        for xx in arr:
            print(xx, end=" ")
        print()
        tc -= 1

# } Driver Code Ends