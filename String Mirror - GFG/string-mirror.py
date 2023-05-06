class Solution:
    def stringMirror(self, str : str) -> str:
        # code here
        
        if len(str)==1:
            return str+str
        
        pre = str[0]
        
        for i in range(1, len(str)):
            if str[i-1]>str[i]:
                pre+=str[i]
            elif len(pre)>1 and str[i-1]==str[i]:
                pre+=str[i]
            else:
                break
        
        return pre+pre[::-1]
        



#{ 
 # Driver Code Starts
if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        
        str = (input())
        
        obj = Solution()
        res = obj.stringMirror(str)
        
        print(res)
        

# } Driver Code Ends