def sort012(self,arr,n):
    # code here
    left=0
    right=n-1
    mid=0
    
    while mid<=right:
        if arr[mid]==1:
            mid+=1
        elif arr[mid]==0:
            arr[left],arr[mid]=arr[mid],arr[left]
            mid+=1
            left+=1
        else:
            arr[right],arr[mid]=arr[mid],arr[right]
            right-=1
            