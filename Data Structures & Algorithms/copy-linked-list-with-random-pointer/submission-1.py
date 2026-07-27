"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return 
        #create new nodes in between old ones
        curr = head
        while curr:
            copy = Node(curr.val)
            copy.next = curr.next
            curr.next = copy
            curr = copy.next
            #point to the random nodes
        curr = head
        while curr:
            if curr.random:
                curr.next.random = curr.random.next
            curr = curr.next.next
            #saperate the new and old Linked copyRandomList
        curr = head
        newHead = head.next
        copy = newHead

        while curr:
            curr.next = copy.next
            curr = curr.next
            if curr:
                copy.next = curr.next
                copy = copy.next

        return newHead