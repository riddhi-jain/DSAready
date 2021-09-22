#Solution 1 : TLE :(

import math
A = [-163 , -23]

maxi = -math.inf
l = len(A)
for a in range(l):
    summ = A[a]
    maxi = max(maxi , summ)
    for b in range(a+1 , l):
        summ = summ + A[b]
        maxi = max(maxi , summ)
print(maxi)

#Solution 2 : Greedy Approach [Optimized] :D

Arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
current_sum = 0
max_sum = -math.inf
l = len(Arr)
for i in range(l):
    current_sum += Arr[i]
    max_sum = max(max_sum , current_sum)
    if current_sum < 0:
        current_sum = 0
print(max_sum)
            

