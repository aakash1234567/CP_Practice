
class Solution:
    def trappingWater(self, arr,n):
        #Code here
        
        # ans = 0
        # for i in range(n):
        #     max_r = -1
        #     for r in range(i+1,n):
        #         max_r = max(max_r, arr[r])
        #     max_l = -1
        #     for l in range(i-1,-1, -1):
        #         max_l = max(max_l, arr[l])
        #     ans+=max(0, min(max_r, max_l)-arr[i])
        # return ans
        
        left = [0 for i in range(n)]
        right = [0 for i in range(n)]
        last = 0
        for i in range(n-1, -1 ,-1):
            right[i] = last
            last = max(last, arr[i])
        last = 0
        for i in range(n):
            left[i] = last
            last = max(last, arr[i])
        ans = 0
        for i in range(n):
            ans+=max(0, min(left[i], right[i])-arr[i])
        return ans
        
        
        
#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math



def main():
        T=int(input())
        while(T>0):
            
            n=int(input())
            
            arr=[int(x) for x in input().strip().split()]
            obj = Solution()
            print(obj.trappingWater(arr,n))
            
            
            T-=1


if __name__ == "__main__":
    main()



# } Driver Code Ends