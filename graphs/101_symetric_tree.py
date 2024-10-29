# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def checkTrees(self, leftTree: Optional[TreeNode], rightTree: Optional[TreeNode]) -> bool:
        if leftTree is None:
            return rightTree is None
        if rightTree is None:
            return False
        if leftTree.val != rightTree.val:
            return False
        return self.checkTrees(leftTree.left, rightTree.right) and self.checkTrees(leftTree.right, rightTree.left)
        
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return self.checkTrees(root.left, root.right)