#User function template for Python 3

class Solution:
    def majorityElement(self, A, N):
        #Your code here
        
        cnt = 0
        ele = 0
        for i in range(N):
            if cnt==0:
                ele = A[i]
            if ele != A[i]:
                cnt-=1
            else:
                cnt+=1
        s = 0
        for i in range(N):
            if A[i]==ele:
                s+=1
                
        if s>N//2:
            return ele
        return -1


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math

from sys import stdin


def main():
        T=int(input())
        while(T>0):
            
            N=int(input())

            A=[int(x) for x in input().strip().split()]
            
            
            obj = Solution()
            print(obj.majorityElement(A,N))
            
            T-=1


if __name__ == "__main__":
    main()
# } Driver Code Ends