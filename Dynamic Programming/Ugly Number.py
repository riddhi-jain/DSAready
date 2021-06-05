'''Ugly numbers are numbers whose only prime factors are 2, 3 or 5. The sequence 1, 2, 3, 4, 5, 6, 8, 9, 10, 12, 15, … shows the first 11 ugly numbers. By convention, 1 is included. 
Given a number n, the task is to find n’th Ugly number.

Explaination:
The ugly-number sequence is 1, 2, 3, 4, 5, 6, 8, 9, 10, 12, 15, … 
     because every number can only be divided by 2, 3, 5, one way to look at the sequence is to split the sequence to three groups as below: 
     (1) 1×2, 2×2, 3×2, 4×2, 5×2, … 
     (2) 1×3, 2×3, 3×3, 4×3, 5×3, … 
     (3) 1×5, 2×5, 3×5, 4×5, 5×5, …
     We can find that every subsequence is the ugly-sequence itself (1, 2, 3, 4, 5, …) multiply 2, 3, 5. Then we use similar merge method as merge sort, to get every ugly number from the three subsequence. Every step we choose the smallest one, and move one step after.
     
Time complexity - O(n)
Space complexity - O(n)'''

# Function to get the nth ugly number
 
 
def getNthUglyNo(n):
 
    ugly = [0] * n  # To store ugly numbers
 
    # 1 is the first ugly number
    ugly[0] = 1
 
    # i2, i3, i5 will indicate indices for
    # 2,3,5 respectively
    i2 = i3 = i5 = 0
 
    # Set initial multiple value
    next_multiple_of_2 = 2
    next_multiple_of_3 = 3
    next_multiple_of_5 = 5
 
    # Start loop to find value from
    # ugly[1] to ugly[n]
    for l in range(1, n):
 
        # Shoose the min value of all
        # available multiples
        ugly[l] = min(next_multiple_of_2,
                      next_multiple_of_3,
                      next_multiple_of_5)
 
        # Increment the value of index accordingly
        if ugly[l] == next_multiple_of_2:
            i2 += 1
            next_multiple_of_2 = ugly[i2] * 2
 
        if ugly[l] == next_multiple_of_3:
            i3 += 1
            next_multiple_of_3 = ugly[i3] * 3
 
        if ugly[l] == next_multiple_of_5:
            i5 += 1
            next_multiple_of_5 = ugly[i5] * 5
 
    # Return ugly[n] value
    return ugly[-1]
 
# Driver Code
def main():
 
    n = 150
 
    print getNthUglyNo(n)
 
 
if __name__ == '__main__':
    main()
