__author__ = 'hyphen'
# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution:
    # @param root, a tree node
    # @return nothing
    l=[]
    def connect(self, root):
        if root:
            root.next=None
            self.t(root,1)
            pos=1
            for i in range(len(self.l)):
                lj=len(self.l[i])
                for j in range(lj):
                    if j < lj-1:
                        self.l[i][j].next=self.l[i][j+1]
                    else:
                        self.l[i][j].next=None

    def t(self,root,depth):
        if root:
            if len(self.l)<depth:
                self.l.append([root])
            else:
                self.l[depth-1].append(root)
            self.t(root.left,depth+1)
            self.t(root.right,depth+1)