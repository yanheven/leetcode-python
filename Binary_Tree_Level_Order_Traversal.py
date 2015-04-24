__author__ = 'hyphen'
# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of lists of integers
    def levelOrder(self, root):
        l=[]
        def t(root,depth):
            if root:
                if len(l)<depth:
                    l.append([root.val])
                else:
                    l[depth-1].append(root.val)
                t(root.left,depth+1)
                t(root.right,depth+1)
        t(root,1)
        return l