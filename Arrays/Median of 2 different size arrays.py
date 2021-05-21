'''Given two sorted arrays, a[] and b[], the task is to find the median of these sorted arrays, in O(log n + log m) time complexity, when n is the number of elements in the first array, and m is the number of elements in the second array.

Approach: The given arrays are sorted, so merge the sorted arrays in an efficient way and keep the count of elements inserted in the output array or printed form. So when the elements in the output array are half the original size of the given array print the element as a median element. There are two cases: 

Case 1: m+n is odd, the median is at (m+n)/2 th index in the array obtained after merging both the arrays.
Case 2: m+n is even, the median will be average of elements at index ((m+n)/2 – 1) and (m+n)/2 in the array obtained after merging both the arrays'''

# A Simple Merge based O(n) solution to find
# median of two sorted arrays

""" This function returns median of ar1[] and ar2[].
Assumption in this function:
Both ar1[] and ar2[] are sorted arrays """
def getMedian(ar1, ar2, n, m) :

	i = 0 # Current index of input array ar1[]
	j = 0 # Current index of input array ar2[]
	m1, m2 = -1, -1
  
	if((m + n) % 2 == 1) :
		for count in range(((n + m) // 2) + 1) :	
			if(i != n and j != m) :		
				if ar1[i] > ar2[j] :
					m1 = ar2[j]
					j += 1
				else :
					m1 = ar1[i]
					i += 1		
			elif(i < n) :		
				m1 = ar1[i]
				i += 1
		
			# for case when j<m,
			else :		
				m1 = ar2[j]
				j += 1	
		return m1
	
	# median will be average of elements
	# at index ((m + n)/2 - 1) and (m + n)/2
	# in the array obtained after merging ar1 and ar2
	else :
		for count in range(((n + m) // 2) + 1) :		
			m2 = m1
			if(i != n and j != m) :	
				if ar1[i] > ar2[j] :
					m1 = ar2[j]
					j += 1
				else :
					m1 = ar1[i]
					i += 1		
			elif(i < n) :		
				m1 = ar1[i]
				i += 1
			
			# for case when j<m,
			else :		
				m1 = ar2[j]
				j += 1	
		return (m1 + m2)//2

# Driver code	
ar1 = [900]
ar2 = [5, 8, 10, 20]

n1 = len(ar1)
n2 = len(ar2)
print(getMedian(ar1, ar2, n1, n2))
