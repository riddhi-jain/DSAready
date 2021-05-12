'''Given an array of intervals where intervals[i] = [starti, endi],
merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

Sample Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Sample Output: [[1,6],[8,10],[15,18]]'''

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        self.intervals = intervals
        intervals.sort()
        
        curr_interval = intervals[0]
        final = []
        
        for x in intervals[1:]:
            
            if curr_interval[1] >= x[0]:
                curr_interval[1] = max(curr_interval[1], x[1])
            else:
                final.append(curr_interval)
                curr_interval = x
        
        final.append(curr_interval)
        return final
        
