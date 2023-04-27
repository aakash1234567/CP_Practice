#{ 
 # Driver Code Starts


#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3

class Solution:
    def removeOuter(self, S):
        # Code here
        open = 0
        close = 0
        ans = ''
        start = 1
        for i in range(len(S)):
            if S[i] == "(":
                open+=1
            elif S[i] == ")":
                close+=1
            if open==close:
                ans+=S[start:i]
                start = i+2
        
        return ans
        

#{ 
 # Driver Code Starts.
if __name__ == '__main__': 
    t = int(input ())
    for _ in range (t):
        s = input()
        ob = Solution()
        res = ob.removeOuter(s)
        print(res)
# } Driver Code Ends