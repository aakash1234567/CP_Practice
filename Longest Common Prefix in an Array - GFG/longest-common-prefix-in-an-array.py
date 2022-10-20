#User function Template for python3

class Solution:
    def longestCommonPrefix(self, arr, n):
        # code here
        arr.sort()
        s = arr[0]
        for i in range(1,n):
            temp = arr[i]
            for j in range(len(s)):
                if s[j]!=temp[j]:
                    if len(s[:j])<len(s):
                        s = s[:j]
                    break
        if len(s):
            return s
        return -1

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        n = int(input())
        arr = [x for x in input().strip().split(" ")]
        
        ob=Solution()
        print(ob.longestCommonPrefix(arr, n))
# } Driver Code Ends