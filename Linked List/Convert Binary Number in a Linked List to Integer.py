'''
Given head which is a reference node to a singly-linked list. The value of each node in the linked list is either 0 or 1. The linked list holds the binary representation of a number.Return the decimal value of the number in the linked list.

Example :

1 ---> 0 ---> 1

Input: head = [1,0,1]
Output: 5
Explanation: (101) in base 2 = (5) in base 10

Approach:
1. Initialize result number to be equal to head value: num = head.val. This operation is safe because the list is guaranteed to be non-empty.
2. Parse linked list starting from the head: while head.next:
     The current value is head.next.val. Update the result by shifting it by one to the left and adding the current value: num = num * 2 + head.next.val.
3. Return num.

Time complexity:O(N).
Space complexity:O(1).
'''


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def getDecimalValue(self, head):
        """
        :type head: ListNode
        :rtype: int
        """
        num = head.val
        while(head.next):
            num = (2*num) + (head.next.val)
            head = head.next
        return num
