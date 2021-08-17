#Problem Statement:
# Given an array nums of n integers, return an array of all the unique quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:

# 0 <= a, b, c, d < n
# a, b, c, and d are distinct.
# nums[a] + nums[b] + nums[c] + nums[d] == target
# You may return the answer in any order.

#Algo: 
# 1. Sort the array.
# 2.Loop over the array and fix the first element of the possible triplet, arr[i].
# 3.Loop over the array and fix the second element of the possible triplet, arr[j] at position i+1.
# 4.Then fix two pointers, one at j + 1 and the other at n – 1. And look at the sum, 
# 5.If the sum is smaller than the required number, increment the first pointer.
# 6.Else, If the sum is bigger, decrease the end pointer to reduce the sum.
# 7.Else, if the sum of elements at two-pointer is equal to given number return true.

def fourSum(nums,target):
    X=sorted(nums)
    i=0
    arr=[]
    while i<=len(nums)-4:
        j=i+1
        while j<=len(nums)-3:
            k=j+1
            z=len(nums)-1
            while k<z:
                if X[i]+X[j]+X[k]+X[z]==target:
                    arr.append([X[i],X[j],X[k],X[z]])
                    k=k+1
                    z=z-1
                elif X[i]+X[j]+X[k]+X[z]>target:
                    z=z-1
                else:
                    k=k+1
            j=j+1
        i=i+1
    Z=[]
    for i in arr:
        if i not in Z:
            Z.append(i)
    return Z
    
nums=list(map(int,input().split()))
target=int(input())
print(fourSum(nums,target))    
    