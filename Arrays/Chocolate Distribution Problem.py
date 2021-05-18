'''Given an array A[ ] of positive integers of size N, where each value represents the number of chocolates in a packet. Each packet can have a variable number of chocolates. There are M students, the task is to distribute chocolate packets among M students such that :
1. Each student gets exactly one packet.
2. The difference between maximum number of chocolates given to a student and minimum number of chocolates given to a student is minimum.

Approach:
Sort the array and then finding minimum of the difference of last and first element of subarrays of length M.'''

class Solution:
    def findMinDiff(self, A,N,M):
        self.A = A
        self.N = N
        self.M = M
        A.sort();
        min_so_far = A[M-1] - A[0];
        for i in range(1,len(A)-M+1):
            curr_min = A[i+M-1] - A[i];
            min_so_far = min(curr_min, min_so_far)
        return min_so_far

if __name__ == '__main__':

    t = int(input())

    for _ in range(t):
        N = int(input())
        A = [int(x) for x in input().split()]
        M = int(input())

        solObj = Solution()

        print(solObj.findMinDiff(A,N,M))
