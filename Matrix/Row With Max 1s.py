'''Given a boolean 2D array of n x m dimensions where each row is sorted. Find the 0-based index of the first row that has the maximum number of 1's.'''


class Solution:

	def rowWithMax1s(self,arr, n, m):
		self.arr = arr
		self.n = n
		self.m = m
		count = 0   # count of max no of 1 so far in any row
		index = -1  # index of row of max no of 1 so far
		for i in range(n):
		    x = m
		    #first occurance of 1 in ith row
		    try:x = arr[i].index(1)
		    except ValueError:pass
		    y = m - x  # number of 1s in ith row
		    if( y > count):
		        count = y
		        index = i
		    else:
		        pass
		 # no row has 1
		if(index == -1):return -1
		else:     return index
#{ 
#  Driver Code Starts
if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n, m = list(map(int, input().strip().split()))
        
        inputLine = list(map(int, input().strip().split()))
        arr = [[0 for j in range(m)] for i in range(n)]
        
        for i in range(n):
            for j in range(m):
                arr[i][j] = inputLine[i * m + j]
        ob = Solution()
        ans = ob.rowWithMax1s(arr, n, m)
        print(ans)
        tc -= 1

# } Driver Code Ends
