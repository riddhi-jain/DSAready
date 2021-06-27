'''There are n children standing in a line. Each child is assigned a rating value given in the integer array ratings.
You are giving candies to these children subjected to the following requirements:
1. Each child must have at least one candy.
2. Children with a higher rating get more candies than their neighbors.
Return the minimum number of candies you need to have to distribute the candies to the children.

 
Example :

Input: ratings = [1,0,2]
Output: 5
Explanation: You can allocate to the first, second and third child with 2, 1, 2 candies respectively.'''

'''
Approach:
The candies are always distributed in terms of increments of 1. Further, while distributing the candies, the local minimum number of candies given to a student is 1. Thus, the sub-distributions always take the following form: \text{1, 2, 3, ..., n}1, 2, 3, ..., n or \text{n,..., 2, 1}n,..., 2, 1. Which, can simply be added using the formula n(n+1)/2n(n+1)/2.

Now, we can view the given rankings as some rising and falling slopes. Whenever the slope is rising, the distribution takes the form: \text{1, 2, 3, ..., m}1, 2, 3, ..., m. Similarly, a falling slope takes the form: \text{k,..., 2, 1}k,..., 2, 1. 

In order to decide where to include the local peak point, n, in the rising slope or the in falling slope, we can observe that in order to satisfy both the right neighbor and the left neighbor criteria, the peak point's count needs to be the max. of the counts determined by the rising and the falling slopes. Thus, in order to determine the number of candies required, the peak point needs to be included in the slope which contains more number of points. The local valley point can also be included in only one of the slopes, but this issue can be resolved easily, since the local valley point will always be assigned a candy count of 1 (which can be subtracted from the next slope's count calculations)
'''

''' Time complexity = O(n) , Space complexity = O(1)'''

class Solution:
    def candy(self, ratings: List[int]) -> int:
        def count(n):
            return (n*(n+1)) //2
        
        candies , up, down, oldslope = 0, 0, 0, 0
        n = len(ratings)
        
        if  n <= 1:return n
        
        for i in range(1, n):
            if ratings[i] < ratings[i-1]:newslope = -1
            elif ratings[i] > ratings[i-1]:newslope = 1
            else: newslope = 0
                
            if (newslope == 0 and oldslope > 0) or (newslope >=0 and oldslope < 0):
                candies += count(up) + count(down) + max(up, down)
                up, down = 0, 0
            if newslope > 0:up += 1
            elif newslope < 0:down +=1
            else: candies += 1
            oldslope = newslope
        candies += count(up) + count(down)+ max(up, down) + 1
        return candies
