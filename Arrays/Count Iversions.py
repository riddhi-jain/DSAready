'''Given an array of integers. Find the Inversion Count in the array. 

Inversion Count: For an array, inversion count indicates how far (or close) the array is from being sorted.
If array is already sorted then the inversion count is 0. If an array is sorted in the reverse order then the inversion count is the maximum.'''

'''Logic: use merge sort to count no. of inversions while merging the two sub-arrays along with those in left and right sub-array.'''

def merge(arr, temp_arr, l, mid, h):
    i = l
    j = mid+1
    k = l
    count = 0
    while(i <= mid and j <= h):
        if arr[i] <= arr[j]:
            temp_arr[k] = arr[i]
            i+=1
            k+=1
        else:
            temp_arr[k] = arr[j]
            count+= mid - i + 1
            j+=1
            k+=1
    while i <= mid:
        temp_arr[k] = arr[i]
        i+=1
        k+=1
    while j <= h:
        temp_arr[k] = arr[j]
        j+=1
        k+=1
    for x in range(l, h+1):
        arr[x] = temp_arr[x]
    return count
def merge_sort(arr, temp_arr, l, h):
    count = 0
    if l < h:
        mid = (l + h)//2
        count+= merge_sort(arr, temp_arr, l, mid)
        count+= merge_sort(arr, temp_arr, mid+1, h)
        count+= merge(arr, temp_arr, l, mid, h)
    return count

class Solution:
    def inversionCount(self, arr, n):
        self.arr = arr
        self.n = n
        temp_arr = [0]*n
        return merge_sort(arr, temp_arr, 0, n-1)

import atexit
import io
import sys

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER

@atexit.register

def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())

if __name__=='__main__':
    t = int(input())
    for tt in range(t):
        n = int(input())
        a = list(map(int, input().strip().split()))
        obj = Solution()
        print(obj.inversionCount(a,n))
