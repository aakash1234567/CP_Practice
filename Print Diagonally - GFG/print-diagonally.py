#User function Template for python3

def downwardDigonal(N, A): 
    # code here 
    ans = []
    for i in range(N):
        k = i
        for j in range(N):
            ans.append(A[j][k])
            k-=1
            if k<0:
                break
    
    col = N-1
    prow=1
    row = 1
    while len(ans)!=N*N:
        ans.append(A[row][col])
        row+=1
        col-=1
        if row==N:
            row=prow+1
            prow=row
            col=N-1
    return ans
#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        matrix =[]
        for i in range(n):
            row = list(map(int, input().strip().split()))
            matrix.append(row)
        ans = downwardDigonal(n,matrix)
        for i in ans:
            print(i,end=" ")
        print()

# } Driver Code Ends