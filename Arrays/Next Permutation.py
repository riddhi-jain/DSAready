'''Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.

If such an arrangement is not possible, it must rearrange it as the lowest possible order (i.e., sorted in ascending order).

The replacement must be in place and use only constant extra memory.'''


'''Algorithm:
Loop from end to start of the list:
If find the swap point(swap point is the current_num < the last_number (largest number) found by previous sort steps):
then find the first larger number in the sorted list and swap with the current number
else:
sort the list from current number'''

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums) - 1
        
        for i in range(1, len(nums)):
            index = n-i 
            if(index >=0):
                if(nums[index] < nums[n]):
                    #swap point recieved
                    for j in range(index, n):
                        swap_num = nums[j + 1]
                        if swap_num > nums[index]:
                            nums[j + 1] = nums[index]
                            nums[index] = swap_num
                            break
                    break;
                else:
                    #sort
                    num = nums[index]
                    del nums[index]
                    for i in range(index, len(nums) - 1):
                        current_num = nums[i]
                        if current_num > num:
                            nums.insert(i, num)
                            return
                    nums.append(num)
                    
        
        
