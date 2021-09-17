'''
A binary string is monotone increasing if it consists of some number of 0's (possibly none), followed by some number of 1's (also possibly none).
You are given a binary string s. You can flip s[i] changing it from 0 to 1 or from 1 to 0.
Return the minimum number of flips to make s monotone increasing.

Example 1:

Input: s = "00110"
Output: 1
Explanation: We flip the last digit to get 00111.
Example 2:

Input: s = "010110"
Output: 2
Explanation: We flip to get 011111, or alternatively 000111.

Approach:
we can keep track of how many flips we need to make the subsequence S[:i] monotone increasing, ending in either '0' or '1'. We store these two numbers in variables flips_0 and flips_1.At the end of DP, we can take the minimum of flips_0 and flips_1 to get the minimum number of flips needed to make S monotone increasing, ending in either '0' or '1'. Here, we only need to keep variables flips_0 and flips_1, so the space is constant O(1).
'''

class Solution(object):
    def minFlipsMonoIncr(self, s):
        """
        :type s: str
        :rtype: int
        """
        min_flips_to_end_0 = 0     # flip_0 in approach
        min_flips_to_end_1 = 0     # flip_1 in approach
        
        for i, x in enumerate(s):
            if x == '0':
                # min_flips_to_end_0 remains unchanged
                min_flips_to_end_1 = min(min_flips_to_end_0, min_flips_to_end_1) + 1
            
            elif x == '1':
                min_flips_to_end_1 = min(min_flips_to_end_0, min_flips_to_end_1)
                min_flips_to_end_0 +=1
                
                
        return min(min_flips_to_end_0, min_flips_to_end_1)
