#User function Template for python3


# m is maximum of number zeroes allowed 
# to flip, n is size of array 
def findZeroes(arr, n, m) :
    # code here
    left = 0
    right = 0
    z = 0
    mx = 0
    while right<n:
        if arr[right]==0:
            z+=1
        while z>m:
            if arr[left]==0:
                z-=1
            left+=1
        right+=1
        mx = max(mx, right-left)
    return mx

#{ 
 # Driver Code Starts
#Initial Template for Python 3




# Driver code 
if __name__ == "__main__": 		
    tc=int(input())
    while tc > 0:
        n=int(input())
        arr=list(map(int , input().strip().split()))
        m=int(input())
        ans= findZeroes(arr, n, m)
        print(ans)
        tc=tc-1
# } Driver Code Ends