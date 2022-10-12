# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # if loop with head is null and head.next is null we will just return head
        if head == None or head.next == None:
            return head
        else:
            temp = head.next # set temp to head.next
            # head.next is set to swapPairs with a parameter of head.next.next
            head.next = self.swapPairs(head.next.next)
            temp.next = head # temp.next is set to the head
        return temp # return temp as the end