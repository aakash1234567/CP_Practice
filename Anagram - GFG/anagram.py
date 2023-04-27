#User function Template for python3


class Solution:
    
    #Function is to check whether two strings are anagram of each other or not.
    def isAnagram(self,a,b):
        #code here
        if len(a) != len(b):
            return False
            
        arr = [0 for i in range(26)]
        
        for i in range(len(a)):
            arr[ord(a[i])-ord('a')] +=1
            arr[ord(b[i])-ord('a')] -=1
        
        for i in range(26):
            if arr[i]!=0:
                return False
        return True
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        a,b=map(str,input().strip().split())
        if(Solution().isAnagram(a,b)):
            print("YES")
        else:
            print("NO") 
# } Driver Code Ends