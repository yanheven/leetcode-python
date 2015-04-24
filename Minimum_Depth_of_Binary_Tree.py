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
    def minDepth(self, root):
        if not root:
            return 0
        ld=self.minDepth(root.left)
        rd=self.minDepth(root.right)
        if ld==rd==0:
            return 1
        if ld and rd:
            return min(ld,rd)+1
        if ld:
            return ld+1
        return rd+1