# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head is None: # if the list is empty
            return head
        if head.next is None: # if the list has only one element
            return None
        curr = head # current node
        for _ in range(n): # move the current node n steps forward
            curr = curr.next
        if curr is None: # if the current node is None, then the head node is the one to be removed
            return head.next
        prev = head # previous node
        while curr.next is not None: # move the current node to the end of the list
            # and the previous node to the node before the one to be removed
            curr = curr.next
            prev = prev.next
        prev.next = prev.next.next
        return head # return the head node
