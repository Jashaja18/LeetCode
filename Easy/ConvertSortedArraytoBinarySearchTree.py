# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums: # if nums is empty
            return None # return None
        else:
            mid = len(nums) // 2 # Find the middle of the array
            root = TreeNode(nums[mid]) # Create a node with the middle value
            root.left = self.sortedArrayToBST(nums[:mid]) # Create the left subtree
            root.right = self.sortedArrayToBST(nums[mid+1:]) # Create the right subtree
            return root # Return the root node