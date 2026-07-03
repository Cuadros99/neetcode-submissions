# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        res = True

        def dfs(root):
            nonlocal res

            if root is None: return 0

            left_depth = dfs(root.left)
            right_depth = dfs(root.right)

            if abs(left_depth - right_depth) > 1:
                res = False

            return max(left_depth, right_depth) + 1

        dfs(root)

        return res
            