class Solution:
    def reverse(self, x: int) -> int:
        y = 0
        temp = x
        if x<0:
            x*=-1
        while x > 0:
            rem = x%10
            x = x//10
            y= y*10 + rem
            p=10
        if temp <0:
            y *= -1
        if y >2**31 -1 or y < -2**31:
            return 0
        return y