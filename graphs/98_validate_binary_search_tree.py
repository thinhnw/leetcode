from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def generate(self, last: int):
        if self.val * 2 <= last:
            self.left = TreeNode(self.val * 2)
            self.left.generate(last)
        if self.val * 2 + 1 <= last:
            self.right = TreeNode(self.val * 2 + 1)
            self.right.generate(last)

class Solution:
    def extrema(self, node: TreeNode) -> list:
        if not node:
            return
        left_min, right_max = node.val, node.val
        if node.left:
            extrema = self.extrema(node.left)
            if node.val <= extrema[1]:
                self.ans = False
            left_min = extrema[0]
            
        if node.right:
            extrema = self.extrema(node.right)
            if node.val >= extrema[0]:
                self.ans = False
            right_max = extrema[1]
        return [left_min, right_max]

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        self.ans = True
        self.extrema(root)
        return self.ans
root = TreeNode(1)
root.generate(4)
print(Solution().isValidBST(root))