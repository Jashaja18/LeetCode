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
        # 1. Create a new node for each node in the original list
        # 2. Connect the new nodes together
        # 3. Connect the random pointers
        # 4. Separate the original list and the new list
        if not head:
            return head

        # 1. Create a new node for each node in the original list
        curr = head
        while curr:
            temp = curr.next
            curr.next = Node(curr.val)
            curr.next.next = temp
            curr = temp

        # 2. Connect the random pointers
        curr = head
        while curr:
            if curr.random:
                curr.next.random = curr.random.next
            curr = curr.next.next

        # 3. Separate the original list and the new list
        curr = head
        new_head = head.next
        while curr:
            temp = curr.next
            curr.next = temp.next
            if temp.next:
                temp.next = temp.next.next
            curr = curr.next

        return new_head
