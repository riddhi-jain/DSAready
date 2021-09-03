'''
A number N is represented in Linked List such that each digit corresponds to a node in linked list. You need to add 1 to it.

Example 1:

Input:
LinkedList: 4->5->6
Output: 457 

Approach:
1. Reverse the linked list to access the ones place digit to perform addition.
2. Now, while the traversal does not reach the list end, check for conditions:
- if node value is not 9: simply increment the value
- if node value is nine and next node is not null: make the value 0 and point current to next
- if node vlue is 9 and next node is null: make the node 0 and create a temp node with value 1, add it to the list end and point current to it
3. Now reverse the list and return head
'''

class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None


class Solution:
    def rev(self, head):
        curr = head
        prev = None
        while(curr is not None):
            nex = curr.next
            curr.next = prev
            prev = curr
            curr = nex
        return prev
        
    def addOne(self,head):
        #Returns new head of linked List.
        self.head = head
        head = self.rev(head)
        curr = head
        bol = True
        while(curr is not None and bol == True):
            if (curr.data == 9 and curr.next != None):
                curr.data = 0
                curr = curr.next
            elif (curr.data == 9 and curr.next == None):
                curr.data = 0
                temp = Node(1)
                curr.next = temp
                temp.next = None
                curr = temp.next
            else:
                curr.data = curr.data + 1
                curr = curr.next
                bol = False
        head = self.rev(head)
        return head
                
        

#{ 
#  Driver Code Starts
#Initial Template for Python 3

# Node Class
class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None

# Linked List Class
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    # creates a new node with given value and appends it at the end of the linked list
    def insert(self, value):
        if self.head is None:
            self.head = Node(value)
            self.tail = self.head
        else:
            self.tail.next = Node(value)
            self.tail = self.tail.next

def PrintList(head):
    while head:
        print(head.data,end='')
        head = head.next

if __name__ == '__main__':
    t=int(input())
    for _ in range(t):
        
        num = input()
        ll = LinkedList() # create a new linked list 'll1'.
        for digit in num:
            ll.insert(int(digit))  # add to the end of the list
        
        resHead = Solution().addOne(ll.head)
        PrintList(resHead)
        print()


# } Driver Code Ends
