'''Given an array arr[] of N non-negative integers representing the height of blocks. If width of each block is 1, compute how much water can be trapped between the blocks during the rainy season.

Approach:
1. Find maximum height of bar from the left end upto an index i in the array, left_max.
2. Find maximum height of bar from the right end upto an index i in the array, right_max.
3. Iterate over the height array and update ans:
Add min(left_max[i],right_max[i])−height[i] to ans 
 
 '''

class Solution:
    def trappingWater(self, arr,n):
        self.arr = arr
        self.n = n
        left = [0]*n
        right = [0]*n
        left[0] = arr[0]
        right[n-1] = arr[n-1]
        
        total_water = 0
        
        for i in range(1,n):
            left[i] = max(left[i-1], arr[i])
        
        for i in range(n-2, -1, -1):
            right[i] = max(right[i+1], arr[i])
            
        for i in range(n):
            total_water += (min(left[i], right[i])-arr[i])
        
        return total_water

import math
def main():
        T=int(input())
        while(T>0):
            
            n=int(input())
            
            arr=[int(x) for x in input().strip().split()]
            obj = Solution()
            print(obj.trappingWater(arr,n))
            T-=1


if __name__ == "__main__":
    main()
