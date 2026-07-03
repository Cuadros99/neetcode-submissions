# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def isRootBetween(root, p, q):
    condition1 = p.val < root.val and root.val < q.val
    condition2 = p.val > root.val and root.val > q.val
    return condition1 or condition2

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if root.val == p.val: return root
        if root.val == q.val: return root

        if isRootBetween(root, p, q):
            return root

        if p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q) 
        else:
            return self.lowestCommonAncestor(root.right, p, q) 





    