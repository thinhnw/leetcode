# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root is None:
            return False
        q = [(root, root.val)]
        index = 0
        while index < len(q):
            u = q[index]
            if u[0].left:
                q.append((u[0].left, u[1] + u[0].left.val))
            if u[0].right:
                q.append((u[0].right, u[1] + u[0].right.val))
            if u[0].left is None and u[0].right is None:
                if u[1] == targetSum:
                    return True
            index += 1
        
        return False
