# Problem statement : 
# Given an array arr[] of size n where every element is in range from 0 to n-1.
# Rearrange the given array so that arr[i] becomes arr[arr[i]]. This should be done with O(1) extra space.
# Time complexity : O(n)
# logic : We cannot create a 2nd array to store the values of both the old and the new values when we change
# So we use the formula => a = a + (b%n)*n 
# therfore : a = a/n and b = b%n
 
def ArrangeBySwappingIndices(A):
    n = len(A)
    for i in range(n):
        A[i] += (A[A[i]] % n) * n
    for i in range(n):
        A[i]//=n;
    for i in range(n):
        print(A[i], end = " ")
A  = [4,0,2,1,3]
print(ArrangeBySwappingIndices(A))    

# Output : 3 4 2 0 1 None
