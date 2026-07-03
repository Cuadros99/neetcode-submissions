# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.output = 0

        def dfs(root, max_val):
            if root is None: return

            if root.val >= max_val:
                self.output += 1
                print(root.val)
                max_val = root.val
            
            dfs(root.left, max_val)
            dfs(root.right, max_val)

        dfs(root, -float('inf'))
        return self.output