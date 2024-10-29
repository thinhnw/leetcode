# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        if root.left is None and root.right is None:
            return 1
        leftDepth = 1e5
        rightDepth = 1e5
        if root.left is not None:
            leftDepth = 1 + self.minDepth(root.left)
        if root.right is not None:
            rightDepth = 1 + self.minDepth(root.right)
                    
        return min(leftDepth, rightDepth)