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
    def level(self, node: Optional[TreeNode]):
        if not node:
            return 0
        return 1 + self.level(node.right)

    def find_last(self, node: Optional[TreeNode]):
        if not node:
            return 0
        return max(node.val, max(self.find_last(node.left), self.find_last(node.right)))

    def check(self, node: Optional[TreeNode], pattern: int, k: int) -> bool:
        if not node:
            return False
        if not k and node:
            return True
        kth_bit = 1 << (k - 1) 
        # print(pattern, bool(pattern & kth_bit))
        if (pattern & kth_bit):
            return self.check(node.right, pattern ^ kth_bit, k - 1)
        return self.check(node.left, pattern, k - 1)

    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        max_level = self.level(root) + 1

        x = 1 << (max_level - 1)
        l = x
        r = (1 << max_level) - 1
        
        while l <= r:
            mid = (l + r) >> 1
            print(l, r, mid, mid - x, max_level - 1)
            if self.check(root, mid - x, max_level - 1):
                l = mid + 1
            else:
                r = mid - 1
        return l - 1


root = TreeNode(1)
root.generate(4)
# print(Solution().check(root, 1, 2))
print(Solution().countNodes(root))