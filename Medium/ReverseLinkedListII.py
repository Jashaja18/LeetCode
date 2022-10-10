# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        # 1. Find the node before the left node
        # 2. Reverse the nodes between left and right
        # 3. Connect the reversed nodes to the left node
        # 4. Connect the left node to the right node
        # 5. Return the head
        if not head:
            return head

        dummy_node = ListNode()
        dummy_node.next = head

        prev = dummy_node

        for i in range(left - 1):
            prev = prev.next
        curr = prev.next

        for i in range(right - left):
            temp = curr.next
            curr.next = temp.next
            temp.next = prev.next
            prev.next = temp

        return dummy_node.next

