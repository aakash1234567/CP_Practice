#User function Template for python3

class Solution:
    def asteroidCollision(self, N, asteroids):
        # Code here
        if N==1:
            return asteroids
        stack = [asteroids[0]]
        i = 1
        def isCollision(asteroids,stack,i):
            if asteroids[i]//stack[-1]<0 and asteroids[i]<=stack[-1]:
                return 1
            return 0
            
        while i<N:
            while i<N and len(stack) and isCollision(asteroids,stack,i):
                if abs(stack[-1])==abs(asteroids[i]):
                    stack.pop()
                    i+=1
                elif abs(stack[-1])>abs(asteroids[i]):
                    i+=1
                else:
                    stack.pop()
            if i<N and (len(stack)==0 or isCollision(asteroids,stack,i)==0):
                stack.append(asteroids[i])
                i+=1
        return stack

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        N = int(input())
        asteroids = list(map(int, input().split()))
        ob = Solution()
        res = ob.asteroidCollision(N, asteroids)
        for val in res:
            print(val, end = ' ')
        print()
# } Driver Code Ends