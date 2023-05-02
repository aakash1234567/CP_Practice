class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # rows = [1 for i in range(len(matrix))]
        # cols = [1 for i in range(len(matrix[0]))]

        # for i in range(len(matrix)):
        #     for j in range(len(matrix[0])):
        #         if matrix[i][j] == 0:
        #             rows[i] = 0
        #             cols[j] = 0
        
        # for i in range(len(matrix)):
        #     for j in range(len(matrix[0])):
        #         if rows[i]==0 or cols[j]==0:
        #             matrix[i][j]=0

        c0 = 1
        r = len(matrix)
        c = len(matrix[0])

        for i in range(r):
            if matrix[i][0]==0:
                c0 = 0
            for j in range(1, c):
                if matrix[i][j]==0:
                    matrix[i][0]=0
                    matrix[0][j]=0
        
        for i in range(r-1,-1,-1):
            for j in range(c-1,0,-1):
                if matrix[i][0]==0 or matrix[0][j]==0:
                    matrix[i][j]=0
            if c0==0:
                matrix[i][0] = 0
            

