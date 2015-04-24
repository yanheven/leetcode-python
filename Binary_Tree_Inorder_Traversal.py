__author__ = 'hyphen'
# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of integers
    def inorderTraversal(self, root):
        l=[]
        def t(root):
            if root:
                t(root.left)
                l.append(root.val)
                t(root.right)
        t(root)
        return l