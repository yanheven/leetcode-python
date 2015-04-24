__author__ = 'hyphen'
# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return an integer
    def maxDepth(self, root):
        if root:
            lt=self.maxDepth(root.left)
            rt=self.maxDepth(root.right)
            if lt>rt:
                return lt+1
            else:
                return rt+1
        else:
            return 0