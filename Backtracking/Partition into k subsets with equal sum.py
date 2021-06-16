'''Given an integer array of N elements, the task is to divide this array into K non-empty subsets such that the sum of elements in every subset is same. All elements of this array should be part of exactly one partition.
Example:

Input : arr = [2, 1, 4, 5, 6], K = 3
Output : Yes
we can divide above array into 3 parts with equal
sum as [[2, 4], [1, 5], [6]]

Approach:
1.we will follow a recursive, depth first approach to solve this problem. So, we have a function that takes the current element index we are to process and also the number of subarrays that are completely formed till now.
2.If all of the elements have been used up and k subarrays have been completely formed, that implies our array is completely aprtitioned. This is the base case for the recursion.
3.For the current element we have k different options. This element at index 'index' can be a part of any of the subarrays. We try out the k options by recursing on them.
4.If any of these recursive calls returns True, then we return from there, else we return False.'''

def makesubarray(self, nums):
    """
    :type nums: List[int]
    :rtype: bool
    """

    # If there are no elemnts, then we can't form any subarray
    if not nums:
        return False

    # Number of elements we have
    L = len(nums)

    # Possible sum of each subarray.
    possible_sum =  sum(nums) // k

    # If the sum can be equally split into k parts then we move on.
    if possible_sum * k != sum(nums):
        return False

    # Reverse sort the array because we want to consider the biggest elements first.
    nums.sort(reverse=True)

    # This array represents the k subarray and their current lengths
    sums = [0 for _ in range(k)]

    # Our recursive dfs function.
    def dfs(index):

        # If we reach the end of array, we check if the subarray was formed or not
        if index == L:
            # If k-1 equal subarrays were formed, kth will be the same as these k-1 and answer should be True in that case.
            return sums.count(sums[0]) == k-1 and sums[0] == possible_sum

        # The current elemnt can belong to any of the k sides (provided their remaining lenghts are >= the size of the currentelemnt)
        for i in range(k):
            # If this elemnt can fit in the space left for the current subarray
            if sums[i] + nums[index] <= possible_sum:
                # Recurse
                sums[i] += nums[index]
                if dfs(index + 1):
                    return True
                # Revert the effects of recursion because we no longer need them for other recursions.
                sums[i] -= nums[index]
        return False        
    return dfs(0)
