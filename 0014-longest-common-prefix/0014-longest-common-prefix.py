class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans = strs[0]
        
        for i in range(1,len(strs)):
            j = 0
            temp = ""
            while j<min(len(strs[i]),len(ans)) and ans[j] == strs[i][j]:
                temp+=ans[j]
                j+=1
            ans = temp
        return ans