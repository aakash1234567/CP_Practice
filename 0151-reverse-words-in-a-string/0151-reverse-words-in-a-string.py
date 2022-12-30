class Solution:
    def reverseWords(self, s: str) -> str:
        ans = []
        i=0
        while i < len(s):
            if s[i]!=" ":
                start = i
                
                while i <len(s) and s[i]!=" ":
                    i+=1
                ans.insert(0,s[start:i])
                i-=1
            i+=1
        return " ".join(ans)