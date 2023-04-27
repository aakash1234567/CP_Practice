# User function Template for python3

class Solution:
    
    #Function to reverse words in a given string.
    def reverseWords(self,S):
        # code here 
        ans = ''
        start = len(S)
        for i in range(len(S)-1,-1,-1):
            if S[i]==".":
                ans+=S[i+1:start]
                ans+="."
                start = i
        ans+=S[i:start]
        return ans
            
                


#{ 
 # Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        s = str(input())
        obj = Solution()
        print(obj.reverseWords(s))

# } Driver Code Ends