class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        ans = ""
        open  = 0
        close = 0
        start = 1
        for i in range(len(s)):
            if s[i] == ")":
                close+=1
            elif s[i] == "(":
                open+=1
            if open==close:
                ans+=s[start:i]
                start = i+2
        return ans