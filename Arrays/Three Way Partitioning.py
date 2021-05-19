'''Given an array of size n and a range [a, b]. The task is to partition the array around the range such that array is divided into three parts.
1) All elements smaller than a come first.
2) All elements in range a to b come next.
3) All elements greater than b appear in the end.
The individual elements of three sets can appear in any order. You are required to return the modified array.

Approach:
Dutch National Flag based Quicksort
https://www.geeksforgeeks.org/3-way-quicksort-dutch-national-flag/ '''

#User function template for Python

class Solution:
    #Function to partition the array around the range such 
    #that array is divided into three parts.
	def threeWayPartition(self, arr, a, b):
	    self.arr = arr
	    self.a = a
	    self.b = b
	    n = len(arr)
	    low = 0
	    mid = 0
	    high = n-1
	    while(mid <= high):
	        if(arr[mid] < a):
	            arr[mid], arr[low] = arr[low], arr[mid]
	            mid+=1
	            low+=1
	        elif(arr[mid] > b):
	            arr[mid], arr[high] = arr[high], arr[mid]
	            high-=1
	        else:
	            mid+=1
#{ 
#  Driver Code Starts
#Initial template for Python

from collections import Counter

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        array = list(map(int, input().strip().split()))
        original = Counter(array)
        a,b = list(map(int, input().strip().split()))
        ob = Solution()
        ob.threeWayPartition(array, a, b)

        k1 = k2 = k3 = 0
        for e in array:
            if e > a:
                k3+=1
            elif e<=a and e>=b:
                k2+=1
            elif e<a:
                k1+=1

        m1 = m2 = m3 = 0
        for e in range(k1):
            if array[e]<a:
                m1+=1
        for e in range(k1, k1+k2):
            if array[e]<=a and array[e]>=b:
                m2+=1
        for e in range(k1+k2, k1+k2+k3):
            if array[e]>=a:
                m3+=1

        flag = False
        if k1==m1 and k2==m2 and k3==m3:
            flag = True
        for e in range(len(array)):
            original[array[e]]-=1
        for e in range(len(array)):
            if original[array[e]]!=0:
                flag = False
        if flag:
            print(1)
        else:
            print(0)

# } Driver Code Ends
