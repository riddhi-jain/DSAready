'''A super ugly number is a positive integer whose prime factors are in the array primes.

Given an integer n and an array of integers primes, return the nth super ugly number.

The nth super ugly number is guaranteed to fit in a 32-bit signed integer.

Approach :
Let k be the size of a given array of prime numbers.
Declare a set for super ugly numbers.
Insert the first ugly number (which is always 1) into the set.
Initialize array multiple_of[k] of size k with 0. Each element of this array is an iterator for the corresponding prime in primes[k] array.
Initialize nextMultipe[k] array with primes[k]. This array behaves like next multiple variables of each prime in given primes[k] array i.e; nextMultiple[i] = primes[i] * ugly[++multiple_of[i]].
Now loop until there are n elements in set ugly. 
a). Find minimum among current multiples of primes in nextMultiple[] array and insert it in the set of ugly numbers. 
b). Then find this current minimum is multiple of which prime. 
c). Increase iterator by 1 i.e; ++multiple_Of[i], for next multiple of current selected prime and update nextMultiple for it.'''

class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        self.n = n
        self.primes= primes
        size = len(primes)
        ugly, dp, index, ugly_nums = 1, [1], [0] * size, [1] * size
        for i in range(1, n):
            # compute possibly ugly numbers and update index
            for j in range(0, size):
                if ugly_nums[j] == ugly:
                    ugly_nums[j] = dp[index[j]] * primes[j]
                    index[j] += 1
            # get the minimum
            ugly = min(ugly_nums)
            dp.append(ugly)
        return dp[-1]
