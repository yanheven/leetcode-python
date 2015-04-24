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
    # @return a list of lists of integers
    def pathSum(self, root, sum):
        self.l=[]
        self.subl=[]
        def pathList(root,sum):
            if root:
                self.subl.append(root.val)
                if not root.left and not root.right:
                    if root.val==sum:
                        self.l.append([x for x in self.subl])
                    self.subl.pop()
                    return
                if root.left:
                    pathList(root.left,sum-root.val)
                if root.right:
                    pathList(root.right,sum-root.val)
                self.subl.pop()
        pathList(root,sum)
        return self.l