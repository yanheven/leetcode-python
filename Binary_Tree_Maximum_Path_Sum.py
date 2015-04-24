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
    max_sum=-65535
    def maxPath(self,root):
            tmp=root.val
            lt=0
            rt=0
            if root.left:
                lt=max(self.maxPath(root.left),0)
                tmp+=lt
            if root.right:
                rt=max(self.maxPath(root.right),0)
                tmp+=rt
            self.max_sum=max(self.max_sum,tmp)
            return root.val+max(lt,rt)
    def maxPathSum(self, root):
        if not root:
            return 0
        self.maxPath(root)
        return self.max_sum