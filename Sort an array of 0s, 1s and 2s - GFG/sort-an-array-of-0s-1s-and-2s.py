#User function Template for python3

class Solution:
    def sort012(self,arr,n):
        # code here
        mid=0
        left=0
        right=n-1
        
        while mid<=right:
            if arr[mid]==1:
                mid+=1
            elif arr[mid]==0:
                arr[mid],arr[left]=arr[left],arr[mid]
                left+=1
                mid+=1
            else:
                arr[mid],arr[right]=arr[right],arr[mid]
                right-=1


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t=int(input())
    for _ in range(t):
        n=int(input())
        arr=[int(x) for x in input().strip().split()]
        ob=Solution()
        ob.sort012(arr,n)
        for i in arr:
            print(i, end=' ')
        print()

# } Driver Code Ends