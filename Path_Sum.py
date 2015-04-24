__author__ = 'hyphen'
# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @param sum, an integer
    # @return a boolean
    def hasPathSum(self, root, sum):
        if not root:
            return False
        if root.val==sum and not root.left and not root.right:
            return True
        if root.left:
            lt=self.hasPathSum(root.left,sum-root.val)
            if lt:
                return True
        if root.right:
            rt=self.hasPathSum(root.right,sum-root.val)
            if rt:
                return True
        return False