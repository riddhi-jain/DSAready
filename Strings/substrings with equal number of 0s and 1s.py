''' Given a binary string str of length N, the task is to find the maximum count of substrings str can be divided into such that all the substrings are balanced i.e. they have equal number of 0s and 1s. If it is not possible to split str satisfying the conditions then print -1.
Example: 
Input: str = “0100110101” 
Output: 4 
The required substrings are “01”, “0011”, “01” and “01”.

Approach:
Initialize count = 0 and traverse the string character by character and keep track of the number of 0s and 1s so far, whenever the count of 0s and 1s become equal increment the count. If the count of 0s and 1s in the original string is not equal then print -1 else print the value of count after the traversal of the complete string.'''

s = str(input())
count_sub = 0
count_0 = 0 
count_1 = 0 
for i in range(len(s)):
    if (s[i]== '0'):count_0 += 1 
    else:count_1 += 1 
    if(count_0 == count_1):count_sub += 1 
print(count_sub)
