#User function Template for python3




def getFloorAndCeil(arr, n, x):
    # # code here
    # left = 0
    # right = n-1
    # ceil = -1
    # while left<=right:
    #     mid = (left+right)//2
    #     if arr[mid]==x:
    #         ceil = arr[mid]
    #         break
    #     elif arr[mid]<x:
    #         left=mid+1
    #     else:
    #         ceil=arr[mid]
    #         right=mid-1
            
    # left = 0
    # right = n-1
    # floor = -1
    # while left<=right:
    #     mid = (left+right)//2
    #     if arr[mid]==x:
    #         floor = arr[mid]
    #         break
    #     elif arr[mid]<x:
    #         floor=arr[mid]
    #         left=mid+1
    #     else:
    #         right=mid-1
            
    # return [floor, ceil]
    
    
    floor = -1
    ceil = -1
    
    for i in range(n):
        if arr[i]==x:
            floor = arr[i]
            ceil = arr[i]
            break
        elif arr[i]<x and floor < arr[i]:
            floor = arr[i]
        elif arr[i]>x and (ceil > arr[i] or ceil==-1):
            ceil = arr[i]
    return [floor, ceil]












#{ 
 # Driver Code Starts
#Initial Template for Python 3



if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n, x = list(map(int, input().strip().split()))
        arr = list(map(int, input().strip().split()))

        ans = getFloorAndCeil(arr, n, x)
        print(str(ans[0]) + " " + str(ans[1]))
        tc -= 1

# } Driver Code Ends