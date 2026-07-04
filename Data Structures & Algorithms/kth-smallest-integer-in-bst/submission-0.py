# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        counter = 1
        res = None

        def dfs(root):
            nonlocal res, counter

            if root is None: return

            dfs(root.left)

            if counter == k:
                res = root.val
            counter += 1

            dfs(root.right)

        dfs(root)

        return res

