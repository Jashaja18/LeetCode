# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root == None: # if the root is None return True
            return True
        else: # if the root is not None return the result of the isMirror function
            return self.isMirror(root.left, root.right)

    def isMirror(self, left: Optional[TreeNode], right: Optional[TreeNode]) -> bool:
        if left == None and right == None: # if both left and right are None return True
            return True
        elif left == None or right == None: # if only one of left and right is None return False
            return False
        else: # if both left and right are not None return the result of the isMirror function
            return left.val == right.val and self.isMirror(left.left, right.right) and self.isMirror(left.right, right.left)
