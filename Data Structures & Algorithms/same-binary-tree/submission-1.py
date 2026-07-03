# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        output = True

        def dfs(r1: List(TreeNode), r2: List(TreeNode)):
            nonlocal output
            
            if r1 is None:
                if r2:
                    output = False
                return
            else:
                if r2 is None:
                    output = False
                    return

            if r1.val != r2.val:
                output = False
                return

            dfs(r1.left, r2.left)
            dfs(r1.right, r2.right)

        dfs(p, q)

        return output