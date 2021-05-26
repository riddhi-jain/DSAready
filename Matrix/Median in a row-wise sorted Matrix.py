'''Given a row wise sorted matrix of size RxC where R and C are always odd, find the median of the matrix.

Approach:
An efficient approach for this problem is to use binary search algorithm. The idea is that for a number to be median there should be exactly (n/2) numbers which are less than this number. So, we try to find the count of numbers less than all the numbers.'''


from bisect import bisect_right as upper_bound
MAX = 100
class Solution:
    def median(self, matrix, r, c):
    	self.matrix = matrix
    	self.r = r
    	self.c = c
    	
    	least = matrix[0][0]
    	most = 0
    	for i in range(r):
    	    if matrix[i][0] < least:least = matrix[i][0]
    	    if matrix[i][c-1] > most: most = matrix[i][c-1]
    	
    	required = (r*c+1) // 2
    	while( least < most):
    	    mid = least + (most- least)//2
    	    place = [0]
    	    for i in range(r):
    	        j = upper_bound( matrix[i], mid)
    	        place[0]= place[0] + j
    	        
    	    if place[0] < required:least = mid + 1
    	    else :most = mid
    	return least
#{ 
#  Driver Code Starts


if __name__ == '__main__': 
    ob = Solution()
    t = int (input ())
    for _ in range (t):
        r,c = map(int,input().strip().split())
        matrix = [[0 for j in range(c)] for i in range(r)]
        line1 = [int(x) for x in input().strip().split()]       
        k = 0
        for i in range(r):
            for j in range (c):
                matrix[i][j]=line1[k]
                k+=1
        ans = ob.median(matrix, r, c);
        print(ans)
# } Driver Code Ends
