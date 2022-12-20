#User function Template for python3

class Solution:
    
    #Function to return a list containing the union of the two arrays.
    def mergeArrays(self,a,b,n,m):
        '''
        :param a: given sorted array a
        :param n: size of sorted array a
        :param b: given sorted array b
        :param m: size of sorted array b
        :return:  The union of both arrays as a list
        '''
        # code here 
        ptr1 = 0
        ptr2 = 0
        ans = []
        while ptr1<n and ptr2<m:
            if a[ptr1] <= b[ptr2]:
                if (len(ans)==0 or ans[-1]!=a[ptr1]):
                    ans.append(a[ptr1])
                ptr1+=1
            else:
                if (len(ans)==0 or ans[-1]!=b[ptr2]):
                    ans.append(b[ptr2])
                ptr2+=1
        if ptr1!=n:
            for i in range(ptr1,n):
                if ans[-1]!=a[i]:
                    ans.append(a[i])
        if ptr2!=m:
            for i in range(ptr2,m):
                if ans[-1]!=b[i]:
                    ans.append(b[i])
        return ans
        

#{ 
 # Driver Code Starts
#Initial Template for Python 3

# Contributed by : Nagendra Jha
# Modified by : Sagar Gupta


if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases) :
        n,m = map(int,input().strip().split())
        a = list(map(int,input().strip().split()))
        b = list(map(int,input().strip().split()))
        ob=Solution()
        li = ob.mergeArrays(a,b,n,m)
        for val in li:
            print(val, end = ' ')
        print()
# } Driver Code Ends