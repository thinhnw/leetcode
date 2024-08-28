# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
            
    def __init__(self):
        self.res = int(-1e9)
        
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """        
        
        self.visit(root)
        return self.res


    def visit(self, node):
        node.maxBranch = node.val
        leftMax = 0
        rightMax = 0
        if node.left:
            self.visit(node.left)
            leftMax = max(leftMax, node.left.maxBranch)
            node.maxBranch = max(node.maxBranch, node.val + leftMax)
            
        if node.right:
            self.visit(node.right)
            rightMax = max(rightMax, node.right.maxBranch)
            node.maxBranch = max(node.maxBranch, node.val + rightMax)
            

        self.res = max(self.res, node.maxBranch, leftMax + rightMax + node.val)