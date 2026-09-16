# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: TreeNode | None, subRoot: TreeNode | None) -> bool:

        if not root:
            return False
        if not subRoot:
            return False

        if self.isSameTree(root, subRoot):
            return True
        
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
        

    def isSameTree(self, p: TreeNode, q: TreeNode):

        if not p and not q:
            return True
        
        if p and q and p.val == q.val:
            return self.isSameTree(q.left, p.left) and self.isSameTree(q.right, p.right)
        else:
            return False