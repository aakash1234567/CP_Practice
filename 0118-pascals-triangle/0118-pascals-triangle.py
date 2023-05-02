class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        
        # 3 Questions
        # what could be the value at x, y => use nCr => 
        # res = 1
        # for i in range(r):
        #     res = res*(n-i)
        #     res = res//(i+1)
        # return res
        
        # print a given ROW
        # res = 1
        # print(res)        
        # for i in range(1, n):
            # res = res*(n-i)                 ans*(row-col)/col
        #     res = res//(i)
            # print(res)
        
        ans = [[1]]
        for i in range(numRows-1):
            temp = []
            temp.append(1)
            for j in range(1,i+1):
                temp.append(ans[-1][j]+ans[-1][j-1])
            temp.append(1)
            ans.append(temp)
        return ans