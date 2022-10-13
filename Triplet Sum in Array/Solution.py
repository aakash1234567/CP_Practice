class Solution:
     
    # 2 pointer approach N^2
    def find3Numbers(self,A, n, X):
        # Your Code Here
        A.sort()
        for i in range(n):
            left=i+1
            right=n-1
            while left<right:
                if A[left]+A[right]+A[i]==X:
                    return True
                elif A[left]+A[right]+A[i]>X:
                    right-=1
                else:
                    left+=1
        return False