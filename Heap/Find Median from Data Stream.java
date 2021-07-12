/* The median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value and the median is the mean of the two middle values.

For example, for arr = [2,3,4], the median is 3.
For example, for arr = [2,3], the median is (2 + 3) / 2 = 2.5.

Example :

Input
["MedianFinder", "addNum", "addNum", "findMedian", "addNum", "findMedian"]
[[], [1], [2], [], [3], []]
Output
[null, null, null, 1.5, null, 2.0]

Explanation
MedianFinder medianFinder = new MedianFinder();
medianFinder.addNum(1);    // arr = [1]
medianFinder.addNum(2);    // arr = [1, 2]
medianFinder.findMedian(); // return 1.5 (i.e., (1 + 2) / 2)
medianFinder.addNum(3);    // arr[1, 2, 3]
medianFinder.findMedian(); // return 2.0 */

/* approach:
building a minheap for elemnts right to the middle element and a maxheap for elements to the left of the middle element.
adding each coming element to the respectrive heap according to the heap root and considering root elements for calculating median.
If number of elements in  the array is even, median = mean of (n/2)th and (n/2 + 1) th element i.e minheap.root + maxheap.root / 2
If number of elements in array is odd, median middle element = (n/2)th element = maxheap.root */

class MedianFinder {
 
    PriorityQueue<Integer> min ;
    PriorityQueue<Integer> max ;
    
    public MedianFinder() {
        min  = new PriorityQueue<>();
        max  = new PriorityQueue<>( Comparator.reverseOrder());
    }
    
    public void addNum(int num) {
        
        if( min.isEmpty() && max.isEmpty() )
            max.add(num);
        
        else if( num > max.peek() ) {
            min.add(num);            
            if( min.size() - max.size() >= 2) {
                max.add(min.poll());    
            }
                
        }
        else {
            max.add(num);            
            if( max.size() - min.size() >= 2 ) {
                min.add(max.poll());    
            }
            
        }
        
    }
    
    public double findMedian() {
        
        if( max.size() == min.size() ) {
            double ans = (double)max.peek() + (double)min.peek();
            ans = ans / (double)2;
            return ans ;
        }
    
        if( min.size() > max.size() ) 
            return (double)min.peek();
    
        return (double)max.peek();
    }

    
}
/**


 * Your MedianFinder object will be instantiated and called as such:
 * MedianFinder obj = new MedianFinder();
 * obj.addNum(num);
 * double param_2 = obj.findMedian();
 */
