class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        cnt = 0
        a,b,c = -1,-1,-1
        for i in range(len(s)):
            if s[i]=='a':
                a=i
            elif s[i]=='b':
                b=i
            else:
                c=i
            cnt += min([a,b,c])+1
        return cnt