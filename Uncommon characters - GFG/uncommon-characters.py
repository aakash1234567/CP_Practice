#User function Template for python3

class Solution:
    def UncommonChars(self,A, B):
        #code here
        a = [0]*26
        b = [0]*26
        ans=''
        for i in range(len(A)):
            a[ord(A[i])-ord('a')]=1
        for i in range(len(B)):
            b[ord(B[i])-ord('a')]=1
        for i in range(26):
            if (a[i] and b[i]!=1) or (a[i]!=1 and b[i]):
                ans+=chr(ord('a')+i)
        if ans:
            return ans
        return -1 

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    T = int(input())

    for tcs in range(T):
        A = input()
        B = input()
        ob = Solution()
        print(ob.UncommonChars(A, B))

# } Driver Code Ends