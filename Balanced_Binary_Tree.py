__author__ = 'hyphen'
# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a boolean
    flag=True
    def isBalanced(self, root):
        self.t(root)
        return self.flag
    def t(self,root):
            if not self.flag:
                return 0
            if root:
                ld=self.t(root.left)
                if not self.flag:
                    return 0
                rd=self.t(root.right)
                if not self.flag:
                    return 0
                if abs(ld-rd)>1:
                    self.flag=False
                return max(ld,rd)+1
            else:
                return 0