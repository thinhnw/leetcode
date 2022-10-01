# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def dfs(self, node, level):
        if not node:
            return
        if level >= len(self.ans):
            self.ans.append([])
        self.ans[level].append(node.val)
        if node.left:
            self.dfs(node.left, level + 1)
        if node.right:
            self.dfs(node.right, level + 1)
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        self.ans = []
        self.dfs(root, 0)
        return self.ans