# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        result = 0

        def dfs(self, root: Optional[TreeNode]) -> int:
            if root is None:
                return 0
            left = dfs(self, root.left)
            right = dfs(self, root.right)
            self.result = max(self.result, left + right)
            return max(left, right) + 1