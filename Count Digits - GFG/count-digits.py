#User function Template for python3


class Solution:
    def evenlyDivides (self, N):
        # code here
        
        ans = 0
        chk = N
        while N > 0:
            rem = N%10
            N = N//10
            
            if rem!=0 and chk%rem==0:
                ans+=1
        return ans


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N = int(input())
       

        ob = Solution()
        print(ob.evenlyDivides(N))
# } Driver Code Ends