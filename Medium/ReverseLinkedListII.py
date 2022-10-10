# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:

        # set two pointers
        slow = fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        prev = None

        # slow pointer: reverse the list
        while slow:
            slow.next, prev, slow = prev, slow, slow.next
            first, second = head, prev

        # once reversed the element is combined back together
        while second.next:
            first.next, first = second, first.next
            second.next, second = first, second.next

