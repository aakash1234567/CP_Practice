class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s)!=len(goal):
            return False
        
        s += s
        j = 0
        for i in range(len(s)):
            if j == len(goal):
                return True
            if s[i]==goal[j]:
                j+=1
            else:
                if s[i]==goal[0]:
                    j=1
                else:
                    j=0
        return False
        